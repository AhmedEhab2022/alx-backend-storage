#!/usr/bin/env python3
"""
This module contains get_page function
"""
import requests
import redis
from typing import Callable
from functools import wraps

r = redis.Redis()

def cache_page(func: Callable) -> Callable:
    """
    Cache the result of the get_page function in Redis
    """
    @wraps(func)
    def wrapper(url):
        """Wrapper function"""
        key = f"count:{url}"
        if r.exists(key):
            return r.get(key)
        else:
            result = func(url)
            r.set(key, result, ex=10)
            return result
        return wrapper

@cache_page    
def get_page(url: str) -> str:
    """Get the content of a web page."""
    response = requests.get(url)
    return response.text
