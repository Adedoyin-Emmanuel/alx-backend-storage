#!/usr/bin/env python3
"""A python function that changes all topics of a
school document based on the name:

Prototype: def update_topics(mongo_collection, name, topics):
mongo_collection will be the pymongo collection object
name (string) this is  the school name to update
topics (list of strings) will be the list of topics approached
in the school
"""


import pymongo


def update_topics(mongo_collection, name, topics):
    """This, changes all topics of a school document"""
    return mongo_collection.update_many({"name": name},
                                        {"$set": {"topics": topics}})
