from bank import Bank
from creation import create_customer, login
from atm import atm

bank = Bank()
bank.load_from_json()

while True:
    print("\n========== BANK ==========") 
    print("1. Create customer") 
    print("2. Login") 
    print("3. ATM") 
    print("4. Exit") 
    print("==========================")

    option = input("Select an option: ")
    match option:
        case "1":
            create_customer(bank)

        case "2":
            login(bank)

        case "3":
            atm(bank)

        case "4": 
            bank.save_to_json()
            print("Exiting") 
            break 

        case _: 
            print("Invalid option")