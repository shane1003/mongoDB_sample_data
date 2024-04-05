def individual_account(account) -> dict:
    return{
        "id": str(account["_id"]),
        "account_id": account["account_id"],
        "limit": account["limit"],
        "products": account["products"] 
    }

def list_account(accounts) -> list:
    return[individual_account(account) for account in accounts]

def individual_customer(customer) -> dict:
    return{
        "id": str(customer["_id"]),
        "username": customer("username"),
        "name": customer["name"], 
        "address": customer["address"],
        "birthdate": customer["birthdate"],
        "email": customer["email"] ,
        "active": customer.get("active"),
        "accounts": customer["accounts"],
        "tier_and_details": customer["tier_and_details"]
    }

def list_customer(customers) -> list:
    return[individual_customer(customer) for customer in customers]

def individual_transaction(transaction) -> dict:
    return{
        "id": str(transaction["_id"]),
        "account_id": transaction["account_id"],
        "transcation_count": transaction["transaction_count"],
        "bucket_start_date": transaction["bucket_start_date"],
        "bucket_end_date": transaction["bucket_end_date"],
        "transactions": transaction["transactions"]
    }

def list_transcation(transcations) -> list:
    return[individual_transaction(transaction) for transaction in transcations]

