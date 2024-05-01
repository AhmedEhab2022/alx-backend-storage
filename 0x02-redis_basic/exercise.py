#!/usr/bin/env python3
"""This module contains class Cache"""
import redis
from typing import Union, Callable
import uuid
import functools


def count_call(method: Callable) -> Callable:
    """
    Decorator that takes a method and returns a new method
    that increments the count for that key every time the
    method is called.
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function"""
        # Generate the key using the qualified name of the method
        key = method.__qualname__
        # Increment the count for the key
        self._redis.incr(key)
        # Call the original method and return the result
        return method(self, *args, **kwargs)
    # Return the wrapper
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Decorator that takes a method and returns a new method
    that stores the history of inputs and outputs for a method.
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function"""
        # Generate the key using the qualified name of the method
        key = method.__qualname__
        # Store the input and output in the history
        self._redis.rpush(key + ":inputs", str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush(key + ":outputs", str(result))
        # Return the result
        return result
    # Return the wrapper
    return wrapper


def replay(method: Callable) -> None:
    """
    Display the history of calls of a particular function.
    """
    # Get the qualified name of the method
    key = method.__qualname__
    # Get the instance of the class
    self = method.__self__
    # Get the count for the key
    count = self._redis.get(key).decode("utf-8")
    # Get the inputs and outputs
    inputs = self._redis.lrange(key + ":inputs", 0, -1)
    outputs = self._redis.lrange(key + ":outputs", 0, -1)
    # Display the history
    print(f"{key} was called {count} times:")
    for i, (input, output) in enumerate(zip(inputs, outputs)):
        print(f"{key}(*{input.decode('utf-8')}) -> {output.decode('utf-8')}")


class Cache:
    """
    Cache class

    Attributes:
        redis: private redis attribute

    Methods:
        store: takes a data argument and returns a string and
               generate a random key (e.g. using uuid),
               store the input data in Redis using the random key
               and return the key.

        get: takes a key string argument and an optional callable argument
             named fn. This callable will be used to convert the data back
             to the desired format.

        get_str: will automatically parametrize Cache.get with
                 the string conversion function.

        get_int: will automatically parametrize Cache.get with
                 the integer conversion function.
    """
    def __init__(self):
        """Constructor method"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_call
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        takes a data argument and returns a string and
        generate a random key (e.g. using uuid),
        store the input data in Redis using the random key
        and return the key
        """
        randKey = str(uuid.uuid1())
        self._redis.set(randKey, data)
        return randKey

    def get(self, key: str, fn: Callable = None):
        """
        takes a key string argument and an optional callable argument
        named fn. This callable will be used to convert the data back
        to the desired format.
        """
        data = self._redis.get(key)
        if fn:
            return fn(data)
        return data

    def get_str():
        """
        will automatically parametrize Cache.get with
        the string conversion function.
        """
        return self.get(key, str)

    def get_int():
        """
        will automatically parametrize Cache.get with
        the integer conversion function.
        """
        return self.get(key, int)
