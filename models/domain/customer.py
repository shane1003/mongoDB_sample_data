from typing import Optional, List
from pydantic import BaseModel, EmailStr

class customer(BaseModel):
    username: str
    name: str
    address: str
    birthday: str
    email: EmailStr
    active: Optional[bool]
    accounts: List[str]
    tier_and_detail: object