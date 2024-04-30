#!/usr/bin/env python3
"""
This module contains a function that returns the list of school
having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    returns the list of school having a specific topic
    mongo_collection will be the pymongo collection object
    topic (string) will be topic searched
    """
    return mongo_collection.find({"topics": topic})
