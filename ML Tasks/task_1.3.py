request_spending = {
    "Mahek": {
        "balance": 3000.00,
        "transactions": [
            {"amount": -9000.00, "category": "Creatives"},
            {"amount": 7000.00, "category": "Sponsor"},
            {"amount": -2000.00, "category": "Prize-Money"}
        ]
    },

    "Arham": {
        "balance": 5000.00,
        "transactions": [
            {"amount": 8000.00, "category": "Stalls"},
            {"amount": 7500.00, "category": "Seminars"}
        ]
    },

    "Unnati": {
        "balance": 3500.00,
        "transactions": [
            {"amount": -5000.00, "category": "Attraction"},
            {"amount": 2500.00, "category": "Promo"},
            {"amount": -900.00, "category": "Lighting"},
            {"amount": -3000.00, "category": "Games"}
        ]
    },

    "Gaurang": {
        "balance": 2000.00,
        "transactions": [
            {"amount": 1500.00, "category": "Website"},
            {"amount": 1000.00, "category": "C2C"},
            {"amount": -500.00, "category": "Posters"}
        ]
    }
}

def total_spending(request_spending, account_id: str, category: str) -> float:
    total = 0.0
    transactions = request_spending.get(account_id, {}).get("transactions", [])
    
    for transaction in transactions:
        if transaction["category"] == category and transaction["amount"] < 0:
            total += abs(transaction["amount"])
    
    return total

def account_balance(request_spending, account_id: str) -> float:
    balance = request_spending.get(account_id, {}).get("balance", 0.0)
    
    transactions = request_spending.get(account_id, {}).get("transactions", [])
    
    for transaction in transactions:
        balance += transaction["amount"]
    
    return balance

def money_owed(request_spending, account_id: str) -> float:
    total_owed = 0.0
    transactions = request_spending.get(account_id, {}).get("transactions", [])
    
    for transaction in transactions:
        if transaction["amount"] > 0:
            total_owed += transaction["amount"]
    
    return total_owed


print("Total spending on Creatives for Mahek:", total_spending(request_spending, "Mahek", "Creatives"))

print("Final balance for Arham:", account_balance(request_spending, "Arham"))

print("Total money owed to Unnati:", money_owed(request_spending, "Unnati"))