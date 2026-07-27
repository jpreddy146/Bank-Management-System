import json
import os

file_name = "accounts.json"

# Load accounts
if os.path.exists(file_name):
    with open(file_name, "r") as file:
        accounts = json.load(file)
else:
    accounts = []

while True:

    print("\n===== BANK MANAGEMENT SYSTEM =====")
    print("1. Create Account")
    print("2. View Accounts")
    print("3. Deposit Money")
    print("4. Withdraw Money")
    print("5. Check Balance")
    print("6. Delete Account")
    print("7. Exit")

    choice = input("Enter your choice: ")

    # Create Account
    if choice == "1":

        account_no = input("Enter Account Number: ")
        name = input("Enter Account Holder Name: ")
        balance = float(input("Enter Initial Balance: "))

        account = {
            "account_no": account_no,
            "name": name,
            "balance": balance
        }

        accounts.append(account)

        with open(file_name, "w") as file:
            json.dump(accounts, file, indent=4)

        print("Account Created Successfully!")

    # View Accounts
    elif choice == "2":

        if len(accounts) == 0:
            print("No Accounts Found.")

        else:
            print("\n===== ACCOUNT LIST =====")

            for account in accounts:
                print("Account No :", account["account_no"])
                print("Name       :", account["name"])
                print("Balance    :", account["balance"])
                print("-----------------------------")

    # Deposit Money
    elif choice == "3":

        account_no = input("Enter Account Number: ")

        found = False

        for account in accounts:

            if account["account_no"] == account_no:

                amount = float(input("Enter Deposit Amount: "))
                account["balance"] += amount

                with open(file_name, "w") as file:
                    json.dump(accounts, file, indent=4)

                print("Money Deposited Successfully!")
                found = True
                break

        if not found:
            print("Account Not Found.")

    # Withdraw Money
    elif choice == "4":

        account_no = input("Enter Account Number: ")

        found = False

        for account in accounts:

            if account["account_no"] == account_no:

                amount = float(input("Enter Withdraw Amount: "))

                if amount <= account["balance"]:
                    account["balance"] -= amount

                    with open(file_name, "w") as file:
                        json.dump(accounts, file, indent=4)

                    print("Withdrawal Successful!")
                else:
                    print("Insufficient Balance!")

                found = True
                break

        if not found:
            print("Account Not Found.")

    # Check Balance
    elif choice == "5":

        account_no = input("Enter Account Number: ")

        found = False

        for account in accounts:

            if account["account_no"] == account_no:

                print("Current Balance:", account["balance"])
                found = True
                break

        if not found:
            print("Account Not Found.")

    # Delete Account
    elif choice == "6":

        account_no = input("Enter Account Number: ")

        found = False

        for account in accounts:

            if account["account_no"] == account_no:

                accounts.remove(account)

                with open(file_name, "w") as file:
                    json.dump(accounts, file, indent=4)

                print("Account Deleted Successfully!")
                found = True
                break

        if not found:
            print("Account Not Found.")

    # Exit
    elif choice == "7":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")
