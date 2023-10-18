#!/usr/bin/env python3
"""A python function that inserts a new document
in a collection based on kwargs:

Prototype: def insert_school(mongo_collection, **kwargs):
mongo_collection will be the pymongo collection object
Returns the new _id
"""


import pymongo


def insert_school(mongo_collection, **kwargs):
    """This, inserts a new document in a collection"""
    return mongo_collection.insert(kwargs)
