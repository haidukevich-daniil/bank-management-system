from customer import Customer

def name_enter():
    while True:
        name = input("Enter your name and surname: ").strip().title()
        parts = name.split()

        if len(parts) != 2:
            print("Enter both name and surname")
        else:
            break
    return name 


def age_enter():
    while True:
        try:
            age = int(input("Enter age: "))
            if not Customer.valid_age(age):
                print("You must be at least 16 years old")
                continue
            return age
        except ValueError:
            print("Age must be a number")


def id_enter():
    try:
        id = int(input("Enter ID: "))
    except ValueError:
        print("ID must be a number")
        return None

    return id


def card_check(card):
    while True:
        try:
            code = input("Enter PIN: ")
            card.authorize(code) 
            return True
        except ValueError as e:
            print(e)
            if card.is_blocked:
                return False


def authorization(bank):
    id = id_enter()
    if id is None:
        return

    customer = bank.find_customer_by_id(id)
    if customer is None:
        print("\nCustomer not found")
        return
    
    try:
        password = password_check()
        if customer.authorize(password):
            print("\nAuthorization is successful")
            return customer

    except ValueError as e:
        print(e)


def password_check():
    while True:
        password = input("Enter password: ")

        if len(password) < 8:
            print("Password must contain at least 8 characters")
            continue

        if not any(char.isupper() for char in password):
            print("Password must contain an uppercase letter")
            continue

        if not any(char.islower() for char in password):
            print("Password must contain a lowercase letter")
            continue

        if not any(char.isdigit() for char in password):
            print("Password must contain a number")
            continue

        return password
