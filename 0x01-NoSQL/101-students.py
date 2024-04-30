#!/usr/bin/env python3
"""
This module contains a function that returns a list of students
sorted by average score
"""


def top_students(mongo_collection):
    """
    Returns a list of students sorted by average score
    mongo_collection will be the pymongo collection object
    The top must be ordered
    The average score must be part of each item returns with key = averageScore
    """
    mongo_collection.aggregate([
        {
          "$addFields": {
              "averageScore": {"$avg": "$topics.score"}
          }
        },
        {
          "$sort": {"averageScore": -1}
        },
        {
          "$out": mongo_collection.name
        }
    ])
    return mongo_collection.find()
