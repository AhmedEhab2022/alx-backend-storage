#!/usr/bin/env python3
"""This module contains class Cache"""
import redis
from typing import Union, Callable
import uuid
from functools import wraps


def count_call(method: Callable) -> Callable:
    """
    Decorator that takes a method and returns a new method
    that increments the count for that key every time the
    method is called.
    """
    @wraps(method)
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
