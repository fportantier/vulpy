"""
Vulnerable payment processing code
Should trigger: Payment category instructions, PCI-DSS patterns (if configured)
"""

import json

# VULNERABLE: Storing raw credit card data
def process_payment(card_number, cvv, expiry_date):
    payment_data = {
        "card_number": card_number,  # Should be tokenized
        "cvv": cvv,  # Should never be stored
        "expiry_date": expiry_date
    }
    
    # VULNERABLE: Logging sensitive payment data
    print(f"Processing payment: {json.dumps(payment_data)}")
    
    # VULNERABLE: No PCI-DSS compliance checks
    return {"status": "processed", "transaction_id": "12345"}

# VULNERABLE: Missing encryption for payment data
def store_payment(payment_data):
    with open("payments.json", "a") as f:
        f.write(json.dumps(payment_data) + "\n")
