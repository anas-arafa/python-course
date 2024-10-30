# ATM Simulation Script
# This script simulates a basic ATM system with user authentication and options for deposit or withdrawal.
# Each user is identified by a 4-digit card number and a 6-digit password.
# The system allows users to make deposits and withdrawals in preset amounts or specify their own amount.

print("ATM")  # Displays ATM title

# Placeholder for user account information (commented out for now)
# accounts = ["anas", 4566, "sara", 4562, "omar", 4545, "ms", 4521]

# Prompt the user to input their 4-digit card number and validate its length
while True:
    number = input("Enter the last 4 digits of your card number (4 digits):\n")
    if len(number) != 4:
        print("Invalid input. Please enter exactly 4 digits.")
        continue  # Repeats the prompt if the input is not 4 digits
    else:
        break  # Exits the loop if the input is valid

# Convert the card number input to an integer for comparison
n = int(number)

# Prompt the user to input their 6-digit password and validate its length
while True:
    password = input("Enter your password (6 digits):\n")
    if len(password) != 6:
        print("Invalid input. Please enter exactly 6 digits.")
        continue  # Repeats the prompt if the input is not 6 digits
    else:
        break  # Exits the loop if the input is valid

# Authentication: Check if the card number corresponds to a known user
if n == 4566:
    print("Hello, Anas!")
elif n == 4562:
    print("Hello, Sara!")
elif n == 4545:
    print("Hello, Omar!")
elif n == 4521:
    print("Hello, Ms!")
else:
    print("Card number not recognized. Exiting system.")
    exit()  # Exits the script if the card number does not match any known users

# Prompt the user to choose a transaction option: Deposit or Withdrawal (credit)
options = input("Choose an option:\n1 for Deposit\n2 for Withdrawal\n")
if int(options) == 2:
    # If the user chooses withdrawal, present predefined withdrawal amounts or option to specify another amount
    amount_options = int(input("Choose withdrawal amount:\n1 for 50\n2 for 100\n3 for 200\n4 for 300\n5 for custom amount\n"))
    if amount_options == 1:
        print("Withdrew 50 from your account.")
    elif amount_options == 2:
        print("Withdrew 100 from your account.")
    elif amount_options == 3:
        print("Withdrew 200 from your account.")
    elif amount_options == 4:
        print("Withdrew 300 from your account.")
    elif amount_options == 5:
        # Custom amount for withdrawal
        amount = int(input("Enter the withdrawal amount: "))
        print("Withdrew", amount, "from your account.")
    print("Thank you for using our ATM.")

elif int(options) == 1:
    # If the user chooses deposit, present predefined deposit amounts or option to specify another amount
    amount_options = int(input("Choose deposit amount:\n1 for 50\n2 for 100\n3 for 200\n4 for 300\n5 for custom amount\n"))
    if amount_options == 1:
        print("Deposited 50 to your account.")
    elif amount_options == 2:
        print("Deposited 100 to your account.")
    elif amount_options == 3:
        print("Deposited 200 to your account.")
    elif amount_options == 4:
        print("Deposited 300 to your account.")
    elif amount_options == 5:
        # Custom amount for deposit
        amount = int(input("Enter the deposit amount: "))
        print("Deposited", amount, "to your account.")
    print("Thank you for using our ATM.")

# Note: In a production environment, account balances should be stored and updated, and authentication should be securely managed.
