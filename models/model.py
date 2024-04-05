from typing import Optional, List, Any
from pydantic import BaseModel, EmailStr
import datetime

class account(BaseModel):
    account_id: int
    limit: int
    product: List[str]
    
class customer(BaseModel):
    username: str
    name: str
    address: str
    birthday: str
    email: EmailStr
    active: Optional[bool]
    accounts: list
    tier_and_detail: object

class transaction(BaseModel):
    account_id: int
    transaction_count: int
    bucket_start_date: datetime.datetime
    bucket_end_date: datetime.datetime
    transaction: list