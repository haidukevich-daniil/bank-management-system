from check import authorization, name_enter, password_check, age_enter, id_enter

def create_customer(bank):
    name = name_enter()
    age = age_enter()

    password = password_check()
    bank.create_customer(name, age, password)
    print("Customer created succesfully")
    print(f"Your ID: {len(bank.customers)}")


def create_account(bank, customer):
    if not bank.customers:
        print("No customers available")
        return

    print("\n1. Regular account")
    print("2. Savings account")
    account_type = input("Select account type: ")

    match account_type:
        case "1":
            account = bank.create_account(customer, "regular")
        case "2":
            account = bank.create_account(customer, "savings")
        case _:
            print("Invalid account type")
            return

    print("Account created successfully")
    print(f"Your account ID: {account.account_id}")


def create_card(bank, customer):
    if not bank.accounts:
        print("No accounts available")
        return

    if not customer.accounts:
        print("You don't have any accounts")
        return

    print("\nYour accounts:")
    customer.show_accounts()

    account_id = id_enter()

    if account_id is None:
        print("Account not found")
        return

    account = customer.find_account(account_id)

    card = bank.create_card(account, customer)

    print("Card created successfully")
    print(f"Card number: {card.card_number}")
    print(f"PIN: {card.pin}")


def login(bank):
    customer = authorization(bank)
    if customer is None:
        return

    while True:
        print("\n======= MY BANK =======")
        print("1. My accounts")
        print("2. My cards")
        print("3. Create account")
        print("4. Create card")
        print("5. Delete")
        print("6. Logout")
        print("=======================")

        option = input("Select an option: ")

        match option:
            case "1":
                print("\n======= Accounts =======")

                if not customer.accounts:
                    print("You don't have any accounts")
                    continue

                customer.show_accounts()

            case "2":
                print("\n======= Cards ========")

                if not customer.cards:
                    print("You don't have any cards")
                    continue

                customer.show_cards()

            case "3":
                create_account(bank, customer)

            case "4":
                create_card(bank, customer)

            case "5":
                print("\n======= Delete =======")
                print("1. Delete customer")
                print("2. Delete account")
                print("3. Delete card")
                print("4. Cancel")
                delete_option = input("Select an option: ")

                match delete_option:
                    case "1":
                        bank.delete_customer(customer)
                        return

                    case "2":
                        account_id = id_enter()
                        if account_id is not None:
                            bank.delete_account(account_id, customer)

                    case "3":
                        card_number = input("Enter card number: ")
                        bank.delete_card(card_number)

                    case "4":
                        print("Delete cancelled")
                        return

                    case _:
                        print("Invalid option")

            case "6":
                print("\nLogging out")
                return

            case _:
                print("Invalid option")

