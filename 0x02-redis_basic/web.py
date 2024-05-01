#!/usr/bin/env python3
"""
This module contains get_page function
"""
import requests
import redis


def get_page(url: str) -> str:
    """Get the content of a web page."""
    r = redis.Redis()
    key = f"count:{url}"
    r.incr(key)
    r.expire(key, 10)
    response = requests.get(url)
    return response.text
