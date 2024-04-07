from pymongo import MongoClient

client = MongoClient("MongoURI")

db = client.sample_analytics

collection_accounts = db["accounts"]
collection_customers = db["customers"]
collection_transactions = db["transactions"]