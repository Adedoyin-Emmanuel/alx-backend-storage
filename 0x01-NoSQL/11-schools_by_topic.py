#!/usr/bin/env python3
"""A python function that returns the list of school
having a specific topic:

Prototype: def schools_by_topic(mongo_collection, topic):
mongo_collection is the pymongo collection object
topic (string) is the topic searched
"""


import pymongo


def schools_by_topic(mongo_collection, topic):
    """This returns the list of school having a specific topic"""
    return mongo_collection.find({"topics": topic})
