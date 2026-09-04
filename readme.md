# Banking Management System
 
A command-line banking system written in Python, built as an OOP portfolio project.
 
## Features
 
- Create customers, accounts (regular or savings), and debit cards
- Delete customers, accounts, or individual cards from the "My Bank" menu
- Login with customer ID + password, protected by password strength validation
- ATM flow: card + PIN authorization, deposit, withdraw, transaction history
- Cards auto-block after 3 failed PIN attempts, and the failed-attempt counter resets on a successful login
- Savings accounts accrue interest based on days elapsed since the last calculation
- All data (customers, accounts, cards, transactions) persists to `bank_data.json` between runs, including deletions
## OOP concepts demonstrated
 
- **Inheritance** — `SavingsAccount` extends `Account`
- **Encapsulation** — `balance` is stored as a private `_balance`, exposed only through a read-only `balance` property; there is no setter, so the only way to change it is through `deposit()` / `withdraw()`, which enforce validation
- **Composition** — `Bank` holds `Customer` objects, which hold `Account` and `Card` objects
- **Polymorphism** — `SavingsAccount` overrides `__str__` and `to_dict()`/`from_dict()` to include interest-specific data
## Project structure
 
| File | Responsibility |
|---|---|
| `main.py` | Entry point, top-level menu |
| `bank.py` | `Bank` class — owns all customers/accounts/cards, JSON save/load, deletion |
| `customer.py` | `Customer` class |
| `account.py` | `Account` base class |
| `savings.py` | `SavingsAccount`, interest calculation |
| `card.py` | `Card` class, PIN authorization |
| `transaction.py` | `Transaction` class |
| `check.py` | Input validation (name, age, password, PIN, IDs) |
| `creation.py` | Customer/account/card creation and deletion flows, login menu |
| `atm.py` | ATM menu (deposit, withdraw, balance, history) |
 
## How to run
 
```
python main.py
```
 
Data is loaded automatically from `bank_data.json` on startup (if it exists) and saved back on exit (option 4 from the main menu).
 
## Data persistence
 
All state is saved to a local JSON file via `Bank.save_to_json()` / `Bank.load_from_json()`. Each model class implements its own `to_dict()` / `from_dict()`, and `Bank` re-links objects (customer → account → card) by ID after loading, since JSON has no concept of object references.
 
Deleting a customer, account, or card removes it from the relevant `Bank` list and from the owner's own list. Saving afterward rewrites `bank_data.json`, so deleted records and their transaction history are no longer stored.
