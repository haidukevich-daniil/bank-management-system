from transaction import Transaction

class Account:
    def __init__(self, account_id, owner):
        self.account_id = account_id
        self._balance = 0
        self.owner = owner      
        self.transactions = []      


    def __str__(self):
        return f"Account ID: {self.account_id}\nBalance: {self.balance:.2f}"

    @property
    def balance(self):
        return self._balance

    
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be greater than 0") 

        self._balance += amount
        self.add_transaction("Deposit", amount)


    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be greater than 0")
        
        if self._balance < amount:
           raise ValueError("Insufficient funds")

        self._balance -= amount
        self.add_transaction("Withdraw", amount)


    def add_transaction(self, type, amount):
        transaction = Transaction(type, amount)
        transaction.transaction_id = len(self.transactions) + 1
        self.transactions.append(transaction)


    def show_transactions(self):
        if not self.transactions:
            print("No transactions yet")
            return
        
        for tr in self.transactions:
            print(tr)


    def to_dict(self):
        return {
            "type": "Account",
            "account_id": self.account_id,
            "owner_id": self.owner.customer_id,
            "balance": self.balance,
            "transactions": [t.to_dict() for t in self.transactions]
        }

    @classmethod
    def from_dict(cls, data, owner):
        account = cls(data["account_id"], owner)
        account._balance = data["balance"]
        account.transactions = [Transaction.from_dict(t) for t in data["transactions"]]
        return account 
    