from datetime import datetime
from account import Account
from transaction import Transaction

class SavingsAccount(Account):
    def __init__(self, account_id, owner):
        super().__init__(account_id, owner)
        self.interest_rate = 0.05
        self.last_interest_date = datetime.now()


    def __str__(self):
        return (
            f"Account ID: {self.account_id}\n"
            f"Owner: {self.owner.name}\n"
            f"Balance: ${self.balance:.2f}\n"
            f"Interest rate: {self.interest_rate * 100:.2f}%"
        )


    def apply_interest(self):
        now = datetime.now()

        days = (now - self.last_interest_date).days

        if days == 0:
            print("Interest already applied today")
            return
         
        interest = self._balance * self.interest_rate * days / 365
        self._balance += interest
        self.add_transaction("Interest", interest)
        self.last_interest_date = now


    def to_dict(self):
        data = super().to_dict()
        data["type"] = "SavingsAccount"
        data["interest_rate"] = self.interest_rate
        data["last_interest_date"] = self.last_interest_date.strftime("%Y-%m-%d")
        return data

    @classmethod
    def from_dict(cls, data, owner):
        account = cls(data["account_id"], owner)    
        account._balance = data["balance"]
        account.interest_rate = data["interest_rate"]
        account.last_interest_date = datetime.strptime(data["last_interest_date"], "%Y-%m-%d")
        account.transactions = [Transaction.from_dict(t) for t in data["transactions"]]
        return account