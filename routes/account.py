from fastapi import APIRouter
from models.account import account
from config.database import collection_accounts
from schema.account import list_account, individual_account
from bson import ObjectId

router = APIRouter()

# get all of data from each collection
# GET Request Method
@router.get("")
async def get_accounts():
    accounts = list_account(collection_accounts.find())
    return accounts

# get data by ObjectID
# GET Request Method
@router.get("/{id}")
async def get_account_by_id(id: str):
    account = individual_account(collection_accounts.find_one({"_id": ObjectId(id)}))
    return account
