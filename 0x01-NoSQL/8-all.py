#!/usr/bin/env python3
"""
this module contains a
Python function that lists all documents in a collection
"""

if __name__ == "__main__":
    def list_all(mongo_collection):
        """
        lists all documents in a collection
        Return an empty list if no document in the collection
        mongo_collection will be the pymongo collection object
        """
        return mongo_collection.find()
