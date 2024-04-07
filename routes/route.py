from fastapi import APIRouter
from models.model import account, customer, transaction
from config.database import collection_accounts, collection_customers, collection_transactions
from schema.schemas import list_account, list_customer, list_transcation, individual_account, individual_customer, individual_transaction
from bson import ObjectId

router = APIRouter()

# get all of data from each collection
# GET Request Method
@router.get("/account")
async def get_accounts():
    accounts = list_account(collection_accounts.find())
    return accounts

# GET Request Method
@router.get("/customer")
async def get_customer():
    customers = list_customer(collection_customers.find())
    return customers

# GET Request Method
@router.get("/transaction")
async def get_transaction():
    transactions = list_transcation(collection_transactions.find())
    return transactions

# get data by ObjectID
# GET Request Method
@router.get("/account/{id}")
async def get_account_by_id(id: str):
    account = individual_account(collection_accounts.find_one({"_id": ObjectId(id)}))
    return account

# GET Request Method
@router.get("/customer/{id}")
async def get_customer_by_id(id: str):
    customer = individual_customer(collection_customers.find_one({"_id": ObjectId(id)}))
    return customer

# GET Request Method
@router.get("/transaction/{id}")
async def get_transaction_by_id(id: str):
    transaction = individual_transaction(collection_transactions.find_one({"_id": ObjectId(id)}))
    return transaction