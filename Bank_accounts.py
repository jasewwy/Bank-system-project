from Bank import *

# Function to create an account based on user input
def create_account():
    print("\n--- Create a New Account ---")
    acct_name = input("Enter account holder name: ")
    acct_type = input("Enter account type (1: BankAccount, 2: InterestRewardsAcct, 3: SavingsAcct): ")
    initial_amount = float(input("Enter initial deposit amount: "))

    if acct_type == '1':
        return BankAccount(initial_amount, acct_name)
    elif acct_type == '2':
        return InterestRewardsAcct(initial_amount, acct_name)
    elif acct_type == '3':
        return SavingsAcct(initial_amount , acct_name)
    else:
        print("\nInvalid account type selection!")
        return None

# Function to display the menu and handle user choices
def display_menu():
    print("\n--- Banking System Menu ---")
    print("1. Create a new account")
    print("2. View balance")
    print("3. Deposit money")
    print("4. Withdraw money")
    print("5. Transfer money")
    print("6. Exit")

# Main function to run the program
def main():
    accounts = {}
    while True:
        display_menu()
        choice = input("\nSelect an option (1-6): ")

        if choice == '1':  # Create account
            account = create_account()
            if account:
                accounts[account.name] = account
                print(f"\nAccount for {account.name} created successfully!")

        elif choice == '2':  # View balance
            name = input("Enter account holder name: ")
            if name in accounts:
                accounts[name].get_balance()
            else:
                print("\nAccount not found!")

        elif choice == '3':  # Deposit
            name = input("Enter account holder name: ")
            if name in accounts:
                amount = float(input("Enter amount to deposit: "))
                accounts[name].deposit(amount)
            else:
                print("\nAccount not found!")

        elif choice == '4':  # Withdraw
            name = input("Enter account holder name: ")
            if name in accounts:
                amount = float(input("Enter amount to withdraw: "))
                accounts[name].withdraw(amount)
            else:
                print("\nAccount not found!")

        elif choice == '5':  # Transfer
            sender = input("Enter sender's account name: ")
            if sender in accounts:
                receiver = input("Enter receiver's account name: ")
                if receiver in accounts:
                    amount = float(input("Enter amount to transfer: "))
                    accounts[sender].transfer(amount, accounts[receiver])
                else:
                    print("\nReceiver's account not found!")
            else:
                print("\nSender's account not found!")

        elif choice == '6':  # Exit
            print("\nExiting the banking system. Goodbye!")
            break

        else:
            print("\nInvalid option! Please try again.")

if __name__ == "__main__":
    main()
