from fastapi import APIRouter
from routes import account, customer, transaction

router = APIRouter()
router.include_router(account.router, tags=["account"], prefix="/account")
router.include_router(customer.router, tags=["customer"], prefix="/customer")
router.include_router(transaction.router, tags=["transaction"], prefix="/transaction")