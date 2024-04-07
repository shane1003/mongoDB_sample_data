def individual_account(account) -> dict:
    return{
        "id": str(account.get("_id")),
        "account_id": account.get("account_id"),
        "limit": account.get("limit"),
        "products": account.get("products") 
    }

def list_account(accounts) -> list:
    return[individual_account(account) for account in accounts]

