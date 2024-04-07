from fastapi import APIRouter
from routes import account, customer, transaction

router = APIRouter()
router.include_router(account.router, prefix="/account")
router.include_router(customer.router, prefix="/customer")
router.include_router(transaction.router, prefix="/transaction")