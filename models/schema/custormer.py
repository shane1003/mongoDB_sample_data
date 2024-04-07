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