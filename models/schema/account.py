from bson import ObjectId
from typing import Optional, List
from pydantic import BaseModel

def individual_account(account) -> dict:
    return{
        "id": str(account.get("_id")),
        "account_id": account.get("account_id"),
        "limit": account.get("limit"),
        "products": account.get("products") 
    }

def list_account(accounts) -> list:
    return[individual_account(account) for account in accounts]

def insert_account(account_id: int, limit: int, products: List) -> dict:
    return {
        "account_id": account_id,
        "limit": limit,
        "products": products
    }

class AccounInUpdate(BaseModel):
    account_id : Optional[int] = None
    limit : Optional[int] = None
    products : Optional[List] = None
