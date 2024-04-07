from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

id = os.getenv('id')
password = os.getenv('password')
mongodb_URI = f'mongodb+srv://{id}:{password}@cluster0.8ulfocx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'
client = MongoClient(mongodb_URI)

db = client.sample_analytics

collection_accounts = db["accounts"]
collection_customers = db["customers"]
collection_transactions = db["transactions"]