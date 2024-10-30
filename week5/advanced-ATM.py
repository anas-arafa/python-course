# Advanced ATM Simulation Script
# This script simulates an ATM system with functions for user authentication,
# balance viewing, withdrawals, and deposits. It utilizes functions, error handling,
# and data structures to provide a realistic ATM experience with improved code organization.

# Dictionary to store user account information
# Each account has an account number, a password, and a balance.
accounts = {
    4566: {"name": "Anas", "password": "123456", "balance": 1000},
    4562: {"name": "Sara", "password": "654321", "balance": 1500},
    4545: {"name": "Omar", "password": "111111", "balance": 2000},
    4521: {"name": "Ms", "password": "222222", "balance": 2500}
}

# Function to authenticate the user by verifying account number and password
def authenticate_user():
    """
    Authenticate the user by checking if the provided account number and password
    match an existing account in the 'accounts' dictionary.
    Returns:
        account_number (int): The account number of the authenticated user, or None if authentication fails.
    """
    try:
        # Prompt for account number and ensure it is an integer
        account_number = int(input("Enter the last 4 digits of your card number (4 digits):\n"))
        
        # Check if the account number exists in the accounts dictionary
        if account_number not in accounts:
            print("Card number not recognized. Please try again.")
            return None  # Return None if account number is invalid

        # Prompt for password and check if it matches the account password
        password = input("Enter your password (6 digits):\n")
        if accounts[account_number]["password"] == password:
            print(f"Hello, {accounts[account_number]['name']}!")  # Welcome message
            return account_number  # Return account number if authenticated
        else:
            print("Incorrect password. Please try again.")
            return None  # Return None if password is incorrect
    except ValueError:
        # Handle non-integer input for account number
        print("Invalid input. Please enter numeric values only.")
        return None

# Function to display the current balance for the authenticated user
def display_balance(account_number):
    """
    Display the balance for a given account number.
    Args:
        account_number (int): The account number of the authenticated user.
    """
    balance = accounts[account_number]["balance"]
    print(f"Your current balance is: {balance}.")

# Function to handle the withdrawal process
def withdraw(account_number):
    """
    Process a withdrawal for the authenticated user.
    Allows the user to select from preset withdrawal amounts or enter a custom amount.
    Checks if the user has sufficient funds before completing the withdrawal.
    Args:
        account_number (int): The account number of the authenticated user.
    """
    try:
        # Show the current balance before starting the transaction
        display_balance(account_number)
        
        # Prompt user for withdrawal amount choice
        amount_options = int(input("Choose withdrawal amount:\n1 for 50\n2 for 100\n3 for 200\n4 for 300\n5 for custom amount\n"))

        # Preset withdrawal amounts based on user choice
        if amount_options in [1, 2, 3, 4]:
            amounts = {1: 50, 2: 100, 3: 200, 4: 300}
            amount = amounts[amount_options]  # Get the corresponding amount from dictionary
        elif amount_options == 5:
            amount = int(input("Enter the withdrawal amount: "))  # Custom withdrawal amount
        else:
            print("Invalid choice. Returning to main menu.")
            return  # Return to the main menu if choice is invalid

        # Check if the user has enough balance for the withdrawal
        if accounts[account_number]["balance"] >= amount:
            accounts[account_number]["balance"] -= amount  # Deduct amount from balance
            print(f"Withdrew {amount}. Your new balance is {accounts[account_number]['balance']}.")
        else:
            print("Insufficient funds. Please try a different amount.")
    except ValueError:
        # Handle non-integer input for withdrawal amount choice
        print("Invalid input. Please enter numeric values only.")

# Function to handle the deposit process
def deposit(account_number):
    """
    Process a deposit for the authenticated user.
    Allows the user to select from preset deposit amounts or enter a custom amount.
    Args:
        account_number (int): The account number of the authenticated user.
    """
    try:
        # Show the current balance before starting the transaction
        display_balance(account_number)
        
        # Prompt user for deposit amount choice
        amount_options = int(input("Choose deposit amount:\n1 for 50\n2 for 100\n3 for 200\n4 for 300\n5 for custom amount\n"))

        # Preset deposit amounts based on user choice
        if amount_options in [1, 2, 3, 4]:
            amounts = {1: 50, 2: 100, 3: 200, 4: 300}
            amount = amounts[amount_options]  # Get the corresponding amount from dictionary
        elif amount_options == 5:
            amount = int(input("Enter the deposit amount: "))  # Custom deposit amount
        else:
            print("Invalid choice. Returning to main menu.")
            return  # Return to main menu if choice is invalid

        # Add amount to user's balance
        accounts[account_number]["balance"] += amount
        print(f"Deposited {amount}. Your new balance is {accounts[account_number]['balance']}.")
    except ValueError:
        # Handle non-integer input for deposit amount choice
        print("Invalid input. Please enter numeric values only.")

# Main ATM function to control ATM operations
def atm():
    """
    Main function to simulate ATM operations, including user authentication,
    viewing balance, making withdrawals, and deposits. This function loops
    until the user chooses to exit.
    """
    print("Welcome to the ATM")

    # Attempt to authenticate the user
    account_number = None
    while account_number is None:
        account_number = authenticate_user()

    # Main ATM menu loop
    while True:
        print("\nMain Menu:")
        print("1 - View Balance")
        print("2 - Withdraw")
        print("3 - Deposit")
        print("4 - Exit")
        try:
            # Prompt user for main menu option
            choice = int(input("Choose an option: "))
            if choice == 1:
                display_balance(account_number)  # Show balance
            elif choice == 2:
                withdraw(account_number)  # Process withdrawal
            elif choice == 3:
                deposit(account_number)  # Process deposit
            elif choice == 4:
                print("Thank you for using our ATM. Goodbye!")  # Exit message
                break  # Exit the ATM
            else:
                print("Invalid choice. Please select an option from 1 to 4.")
        except ValueError:
            # Handle non-integer input for menu choice
            print("Invalid input. Please enter a number.")

# Run the ATM system
atm()
