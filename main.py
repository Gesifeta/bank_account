from Bank_Account import BankAccount
import uuid
import pandas
accounts = {}

continue_transaction = True

while continue_transaction:
    print("\nWelcome to Bank Account ")
    print("1. Create a new account ")
    print("2. Make a deposit ")
    print("3. Make a withdraw ")
    print("4. Check balance ")
    print("5. Show all accounts ")
    print("6. Exit ")
    print("*"*100)
    choice = input("Enter your choice: ")
    if choice == "1":
        customer_id = uuid.uuid4()
        account_number = int(input("Enter account number: "))
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        gender = input("Enter your gender: ")
        initial_deposit = input("Enter your initial deposit: ")
        if first_name is not None or last_name is not None or gender is not None or initial_deposit is not None or account_number is not None:
            if account_number not in accounts:
                accounts[account_number] = BankAccount(account_number, first_name, last_name, gender, initial_deposit)
                print("Account created successfully")
            else:
                print("Account already exists")
    elif choice == "2":
        account_number = int(input("Enter account number: ").strip())
        if account_number not in accounts:
            print("Account does not exist")
        else:
            deposit_amount = float(input("Enter your deposit: ").strip())
            accounts[account_number].deposit(deposit_amount)
    elif choice == "3":
        account_number = int(input("Enter account number: ").strip())
        withdraw = int(input("Enter your withdrawal: "))
        if account_number not in accounts:
            print("Account does not exist")
            continue
        else:
            accounts[account_number].withdraw(withdraw)
    elif choice == "4":
        account_number = int(input("Enter account number: "))
        if account_number not in accounts:
            print("Account does not exist")
            continue
        else:
            print(f"Your account balance is = {accounts[account_number].account_balance()}")
    elif choice == "5":
        account_data = [
            {"account_number":accounts[account].account_number,"name": accounts[account].first_name, "last_name": accounts[account].last_name, "initial_deposit": accounts[account].initial_deposit,
             "balance": accounts[account].balance} for account in accounts]
        print_data = pandas.DataFrame(account_data)
        print(print_data)
    elif choice == "6":
        continue_transaction = False
    else:
        print("Invalid choice")
        continue





