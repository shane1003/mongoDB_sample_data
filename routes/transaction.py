from fastapi import APIRouter
from bson import ObjectId
from config.database import collection_transactions
from schema.transaction import individual_transaction, list_transcation

router = APIRouter()

# GET Request Method
@router.get("")
async def get_transaction():
    transactions = list_transcation(collection_transactions.find())
    return transactions

# GET Request Method
@router.get("/{id}")
async def get_transaction_by_id(id: str):
    transaction = individual_transaction(collection_transactions.find_one({"_id": ObjectId(id)}))
    return transaction