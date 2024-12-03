#MINI_PROJECT
accounts = []
find_account = lambda accs, pin: next((acc for acc in accs if acc['pin'] == pin), None)
account_exists = lambda accs, pin: any(acc['pin'] == pin for acc in accs)
update_balance = lambda acc, amount: acc.update({'balance': acc['balance'] + amount}) or True
#OPEN_ACCOUNT
def open_account():
    print("Choice number 1 is selected by the Customer")
    fullname = input("Input Fullname: ")
    pin = input("Please input a pin of your Choice: ")
    initial_balance = float(input("Please input a value to Deposit to Start an Account: "))
    
    if account_exists(accounts, pin):
        print("Account Already Exists with this Pin.")
    else:
        accounts.append({'fullname': fullname, 'pin': pin, 'balance': initial_balance})
        print(f"Account created for {fullname} with an Initial Deposit of {initial_balance}.")
#WITHDRAW_MONEY
def withdraw_money():
    print("Choice number 2 is selected by the Customer")
    pin = input("Please enter your Pin: ")
    amount = float(input("Please enter the amount to Withdraw: "))
    account = find_account(accounts, pin)
    if account:
        if account['balance'] >= amount:
            account['balance'] -= amount
            print(f"Withdrawal successful. New balance: {account['balance']}")
        else:
            print("Insufficient balance.")
    else:
        print("Account not found.")
#DEPOSITE_MONEY        
def deposit_money():
    print("Choice number 3 is selected by the Customer")
    pin = input("Please enter your Pin: ")
    amount = float(input("Please enter the amount to Deposit: "))
    
    account = find_account(accounts, pin)
    if account:
        update_balance(account, amount)
        print(f"Deposit successful. New balance: {account['balance']}")
    else:
        print("Account Not Found.")
#CUSTOMER_BALANCE
def check_customer_balance():
    print("Choice number 4 is selected by the Customer")
    pin = input("Please enter your Pin: ")
    
    account = find_account(accounts, pin)
    if account:
        print(f"Account details: Fullname: {account['fullname']}, Balance: {account['balance']}")
    else:
        print("Account Not Found.")
#OUTPUT_MENU
def main_menu():
    
    while True:
        print("\n        BANKING SYSTEM             ")
        print("\n====================================")
        print("--------Welcome to Time Bank---------")
        print("*************************************")
        print("=<<1. Open a new account          >>=")
        print("=<<2. Withdraw Money              >>=")
        print("=<<3. Deposit Money               >>=")
        print("=<<4. Check Customer & Balance    >>=")
        print("=<<5. Exit/Quit                   >>=")
        print("*************************************")
        choice = input("Select your choice number from the above menu: ")
        if choice == '1':
            open_account()
        elif choice == '2':
            withdraw_money()
        elif choice == '3':
            deposit_money()
        elif choice == '4':
            check_customer_balance()
        elif choice == '5':
            print("Thank you for using Time Bank. Bye!")
            break
        else:
            print("Invalid Choice. Please Try Again.")
print("EXIT",main_menu())
