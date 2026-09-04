from datetime import datetime

class Transaction:
    def __init__(self, transaction_type, amount):
        self.transaction_id = 0
        self.transaction_type = transaction_type
        self.amount = amount
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        return f"ID: {self.transaction_id} | Type: {self.transaction_type} | Amount: ${self.amount:.2f} | Date: {self.date}"

    def to_dict(self):
        return {
            "transaction_id": self.transaction_id,
            "transaction_type": self.transaction_type,
            "amount": self.amount,
            "date": self.date
        }

    @classmethod
    def from_dict(cls, data):
        transaction = cls(data["transaction_type"], data["amount"])
        transaction.transaction_id = data["transaction_id"]
        transaction.date = data["date"]
        return transaction