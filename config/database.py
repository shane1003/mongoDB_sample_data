from pymongo import MongoClient

client = MongoClient("MongoDB URI")

db = client.sample_analytics

collection_accounts = db["accounts"]
collection_customers = db["customers"]
collection_transactions = db["transactions"]