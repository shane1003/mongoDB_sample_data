def individual_account(account) -> dict:
    return{
        "id": str(account.get("_id")),
        "account_id": account.get("account_id"),
        "limit": account.get("limit"),
        "products": account.get("products") 
    }

def list_account(accounts) -> list:
    return[individual_account(account) for account in accounts]

def individual_customer(customer) -> dict:
    return{
        "id": str(customer.get("_id")),
        "username": customer.get("username"),
        "name": customer.get("name"), 
        "address": customer.get("address"),
        "birthdate": customer.get("birthdate"),
        "email": customer.get("email"),
        "active": customer.get("active"),
        "accounts": customer.get("accounts"),
        "tier_and_details": customer.get("tier_and_details")
    }

def list_customer(customers) -> list:
    return[individual_customer(customer) for customer in customers]

def individual_transaction(transaction) -> dict:
    return{
        "id": str(transaction.get("_id")),
        "account_id": transaction.get("account_id"),
        "transcation_count": transaction.get("transaction_count"),
        "bucket_start_date": transaction.get("bucket_start_date"),
        "bucket_end_date": transaction.get("bucket_end_date"),
        "transactions": transaction.get("transactions")
    }

def list_transcation(transcations) -> list:
    return[individual_transaction(transaction) for transaction in transcations]

