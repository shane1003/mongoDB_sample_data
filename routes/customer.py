from fastapi import APIRouter
from bson import ObjectId
from schema.custormer import list_customer, individual_customer
from config.database import collection_customers

router = APIRouter()

# GET Request Method
@router.get("")
async def get_customer():
    customers = list_customer(collection_customers.find())
    return customers

# GET Request Method
@router.get("/{id}")
async def get_customer_by_id(id: str):
    customer = individual_customer(collection_customers.find_one({"_id": ObjectId(id)}))
    return customer