from fastapi import APIRouter
from typing import List
from config.database import collection_accounts
from models.schema.account import list_account, individual_account, insert_account, AccounInUpdate
from models.domain.account import account
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

#POST Method
@router.post("")
async def put_accounts():
    account = insert_account(1000000, 30000, ["test0", "test1"])
    collection_accounts.insert_one(account)

#UPDATE Method for all data / if less varaible, the variable is chnged to null 느낌상 "$set 때문인거 같긴한데..."
@router.put("/{id}")
async def update_all_by_id(id: str):

    _id = ObjectId(id)

    #이 방식으로 하면 나머지 값이 없을 경우에 null로 치환됨.
    #update_info = AccounInUpdate(account_id=1999999, limit=55555, products=["test0", "test1"]).model_dump()

    #collection_accounts.update_one({"_id" : _id}, {"$set" : {"limit" : 33333}}) 1개 만 바꾸기
    #collection_accounts.update_one({"_id" : _id}, {"$set" : {"products" : ["test0"]}}) 배열 자체를 바꾸기
    #collection_accounts.update_one({"_id" : _id}, {"$set" : {"products.0" : "test3"}}) index로 접근(dict의 key 값이 index임)


#DELETE Method
@router.delete("/{id}")
async def delete_by_id(id: str):
    _id = ObjectId(id)
    collection_accounts.find_one_and_delete({"_id" : _id})

