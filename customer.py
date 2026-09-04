from savings import SavingsAccount

class Customer:
    def __init__(self, customer_id, name, age, password):
        self.customer_id = customer_id
        self.name = name
        self.age = age
        self.password = password
        self.accounts = []
        self.cards = []

    def __str__(self):
        return f"ID: {self.customer_id}\nName: {self.name}\nAge: {self.age}"

    def add_account(self, account):
        self.accounts.append(account)

    def show_accounts(self):
        for account in self.accounts:
            if isinstance(account, SavingsAccount):
                account.apply_interest()
                
            print(account)
            

    def add_card(self, card):
        self.cards.append(card)

    def show_cards(self):
        for card in self.cards:
            print(card)


    def authorize(self, code):
        if code != self.password:
            raise ValueError("Wrong password")
        return True 


    def find_account(self, account_id):
        for a in self.accounts:
            if a.account_id == account_id:
                account = a
                return account
        return None


    @staticmethod
    def valid_age(age):
        return age >= 16


    def to_dict(self):
        return {
            "customer_id": self.customer_id,
            "name": self.name,
            "age": self.age,
            "password": self.password,
            "account_ids": [a.account_id for a in self.accounts],
            "card_numbers": [c.card_number for c in self.cards]
        }


    @classmethod
    def from_dict(cls, data):
        return cls(data["customer_id"], data["name"], data["age"], data["password"])