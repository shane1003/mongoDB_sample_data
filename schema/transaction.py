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