from typing import List
from pydantic import BaseModel

class account(BaseModel):
    account_id: int
    limit: int
    product: List[str]