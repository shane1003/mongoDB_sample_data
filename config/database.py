from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

ATLAS_URI = os.getenv("ATLAS_URI")
client = MongoClient(ATLAS_URI)

db = client.sample_analytics

collection_accounts = db["accounts"]
collection_customers = db["customers"]
collection_transactions = db["transactions"]