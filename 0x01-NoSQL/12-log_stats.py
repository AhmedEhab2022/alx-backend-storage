#!/usr/bin/env python3
"""
this module contains a function for log stats
"""
from pymongo import MongoClient


def log_stats():
    """
    function that provides some stats about
    Nginx logs stored in MongoDB
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.Nginx
    print("{:d} logs".format(nginx_collection.count_documents({})))
    print("Methods:")
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        doc_count = nginx_collection.count_documents({"method": method})
        print("\tmethod {}: {:d}".format(method, doc_count))

    print("{:d} status check".format(nginx_collection.count_documents([
        {"method": "GET"},
        {"path": "/status"}
    ])))


if __name__ == "__main__":
    log_stats()
