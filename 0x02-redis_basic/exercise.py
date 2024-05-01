#!/usr/bin/env python3
"""This module contains class Cache"""
import redis
from typing import Union
import uuid


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
