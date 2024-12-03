accounts = {}

def create_account(account_id, initial_balance=0):
    if account_id in accounts:
        print("Account ID already exists.")
    else:
        accounts[account_id] = {
            'balance': initial_balance,
            'transaction_history': []
        }
        print(f"Account {account_id} created with balance ${initial_balance}.")

def deposit(account_id, amount):
    if account_id in accounts:
        if amount > 0:
            accounts[account_id]['balance'] += amount
            accounts[account_id]['transaction_history'].append(f"Deposited: ${amount}")
            print(f"Deposited ${amount} into account {account_id}.")
        else:
            print("Deposit amount must be positive.")
    else:
        print("Account not found.")

def withdraw(account_id, amount):
    if account_id in accounts:
        if 0 < amount <= accounts[account_id]['balance']:
            accounts[account_id]['balance'] -= amount
            accounts[account_id]['transaction_history'].append(f"Withdrew: ${amount}")
            print(f"Withdrew ${amount} from account {account_id}.")
        else:
            print("Insufficient funds or invalid amount.")
    else:
        print("Account not found.")

def check_balance(account_id):
    if account_id in accounts:
        balance = accounts[account_id]['balance']
        print(f"Account {account_id} balance: ${balance}")
    else:
        print("Account not found.")

def get_transaction_history(account_id):
    if account_id in accounts:
        print(f"Transaction history for account {account_id}:")
        for transaction in accounts[account_id]['transaction_history']:
            print(transaction)
    else:
        print("Account not found.")

def main():
    while True:
        print("\nBanking System")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. View Transaction History")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            account_id = input("Enter new account ID: ")
            initial_balance = float(input("Enter initial balance: "))
            create_account(account_id, initial_balance)

        elif choice == "2":
            account_id = input("Enter account ID: ")
            amount = float(input("Enter amount to deposit: "))
            deposit(account_id, amount)

        elif choice == "3":
            account_id = input("Enter account ID: ")
            amount = float(input("Enter amount to withdraw: "))
            withdraw(account_id, amount)

        elif choice == "4":
            account_id = input("Enter account ID: ")
            check_balance(account_id)

        elif choice == "5":
            account_id = input("Enter account ID: ")
            get_transaction_history(account_id)

        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
