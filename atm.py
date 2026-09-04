from check import card_check

def deposit(account):
    try:
        amount = float(input("Enter amount: "))
        account.deposit(amount)
        print("Transaction is successful")
    
    except ValueError as e:
        print(e)


def withdraw(account):
    try:
        amount = float(input("Enter amount: "))
        account.withdraw(amount)
        print("Transaction is successful")

    except ValueError as e:
        print(e)


def atm(bank):
    card_number = input("Enter card number: ")

    card = bank.find_card(card_number)

    if card is None:
        print("Card not found")
        return

    if card_check(card):
        atm_menu(card)


def atm_menu(card):
    while True:
        print("\n======= ATM =======")
        print("1. Check balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transaction history")
        print("5. Exit")
        print("===================")
        option = input("Select an option: ")

        match option:
            case "1":
                print(f"Current balance: {card.account.balance}")

            case "2":
                deposit(card.account)

            case "3":
                withdraw(card.account)

            case "4": 
                card.account.show_transactions()

            case "5":
                print("Exiting")
                return

            case _:
                print("Invalid operation")