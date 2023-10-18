#!/usr/bin/env python3
"""
Log Stats
mprove 12-log_stats.py by adding the top 10 of the most
present IPs in the collection nginx of the database logs
"""


from pymongo import MongoClient

def log_stats():
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs = client.logs.nginx

    total_logs = logs.count_documents({})

    print(f"{total_logs} logs")

    print("Methods:")
    methods = logs.aggregate([
        {"$group": {"_id": "$method", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}}
    ])
    for method in methods:
        print(f"    method {method['_id']}: {method['count']}")

    print(f"{logs.count_documents({'path': '/status'})} status check")

    print("IPs:")
    ips = logs.aggregate([
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ])
    for ip in ips:
        print(f"    {ip['_id']}: {ip['count']}")

if __name__ == "__main__":
    log_stats()
