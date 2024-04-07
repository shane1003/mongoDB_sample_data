from pydantic import BaseModel
from typing import List
from datetime import datetime as dt

class transaction(BaseModel):
    account_id: int
    transaction_count: int
    bucket_start_date: dt
    bucket_end_date: dt
    transaction: List[str]