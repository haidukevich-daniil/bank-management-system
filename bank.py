from check import card_check
from customer import Customer
from account import Account
from card import Card
import random
import json

from savings import SavingsAccount

class Bank:
    def __init__(self):
        self.customers = []
        self.accounts = []
        self.cards = []


    def create_customer(self, name, age, password):
        if self.customers:
            customer_id = self.customers[-1].customer_id + 1
        else:
            customer_id = 1

        customer = Customer(customer_id, name, age, password)
        self.customers.append(customer)


    def create_account(self, customer, account_type="regular"):
        if self.accounts:
            account_id = self.accounts[-1].account_id + 1
        else:
            account_id = 1

        if account_type == "savings":
            account = SavingsAccount(account_id, customer)
        else:
            account = Account(account_id, customer)

        self.accounts.append(account)
        customer.add_account(account)
        return account


    def create_card(self, account, customer):
        card_number = "".join(str(random.randint(0, 9)) for _ in range(16))
        pin = str(random.randint(1000,9999))

        card = Card(card_number, account, pin)
        self.cards.append(card)
        customer.add_card(card)
        return card


    def find_card(self, card_number):
        for c in self.cards:
            if c.card_number == card_number:
                card = c
                return card
        return None


    def find_customer_by_id(self, customer_id):
        for c in self.customers:
            if c.customer_id == customer_id:
                customer = c
                return customer
        return None


    def find_account_by_id(self, account_id):
        for a in self.accounts:
            if a.account_id == account_id:
                return a
        return None


    def delete_customer(self, customer):

        for a in customer.accounts:
            self.accounts.remove(a)

        for c in customer.cards:
            self.cards.remove(c)

        self.customers.remove(customer)

        print("Customer deleted successfully")


    def delete_account(self, account_id, customer):
        account = self.find_account_by_id(account_id)

        if account is None or account.owner != customer:
            print("Account not found")
            return False

        for c in self.cards[:]:
            if c.account == account:
                self.cards.remove(c)
                account.owner.cards.remove(c)

        self.accounts.remove(account)
        account.owner.accounts.remove(account)
        print("Account deleted successfully")


    def delete_card(self, card_number):
        card = self.find_card(card_number)

        if card is None:
            print("Card not found")
            return

        if card_check(card):
            self.cards.remove(card)
            card.account.owner.cards.remove(card)
            print("Card deleted successfully")


    def save_to_json(self, filename="bank_data.json"):
        data = {
            "customers": [c.to_dict() for c in self.customers],
            "accounts": [a.to_dict() for a in self.accounts],
            "cards": [c.to_dict() for c in self.cards]
        }
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)

        print(f"Data saved to {filename}")


    def load_from_json(self, filename="bank_data.json"):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            print("No saved data found, starting fresh")
            return
        except json.JSONDecodeError:
            print("Saved data file is corrupted, starting fresh")
            return

        self.customers = [Customer.from_dict(c) for c in data["customers"]]

        self.accounts = []
        
        for d in data["accounts"]:
            customer = self.find_customer_by_id(d["owner_id"])

            if d["type"] == "SavingsAccount":
                account = SavingsAccount.from_dict(d, customer)
            else:
                account = Account.from_dict(d, customer)

            self.accounts.append(account)
            customer.add_account(account)

        self.cards = []
        for c in data["cards"]:
            account = self.find_account_by_id(c["account_id"])
            card = Card.from_dict(c, account)
            self.cards.append(card)
            account.owner.add_card(card)

        print(f"Data loaded from {filename}")
