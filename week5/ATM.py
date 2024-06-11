print("ATM")
#accounts=["anas", 4566,"sara", 4562,"omar", 4545,,"ms", 4521]
while True:
    number = input("put the full numbers of your card(4 numbers)\n")
    if len(number) != 4:
        print("try again")
        continue
    else:
        break
n = int(number)
while True:
    password = input("put your password (6 numbers)\n")
    if len(password) != 6:
        print("try again")
        continue
    else:
        break


if number ==4566:
    print("hello_anas")
elif number ==4562:
    print("hello_sara")
elif number ==4545:
    print("hello_omar")
elif number ==4521 :
    print("hello_ms")



options = input("1 for deposit \n2 for credit \n")
if int(options) == 2:
    amount_options = int(input("1 for 50 \n2 for 100 \n3 for 200\n4 for 300\n5 for other \n"))
    if amount_options == 1:
        print("we take from your  account 50 .")
        print("thank you for using our ATM")
    elif amount_options == 2:
        print("we take from your  account  100 .")
        print("thank you for using our ATM")
    elif amount_options == 3:
        print("we take from your  account  200 .")
        print("thank you for using our ATM")
    elif amount_options == 4:
        print("we take from your  account  300 .")
        print("thank you for using our ATM")
    elif amount_options == 5:
        amount = int(input("put the another number"))
        print("we take from your  account ", amount, )
        print("thank you for using our ATM")

if int(options) == 1:
    amount_options = int(input("1 for 50 \n2 for 100\n3 for 200 \n4 for 300\n5 for other \n"))
    if amount_options == 1:
        print("we put to your  account 50 .")
        print("thank you for using our ATM")
    elif amount_options == 2:
        print("we  put to your  account  100 .")
        print("thank you for using our ATM")
    elif amount_options == 3:
        print("we  put to your  account  200 .")
        print("thank you for using our ATM")
    elif amount_options == 4:
        print("we  put to your  account 300 .")
        print("thank you for using our ATM")
    elif amount_options == 5:
        amount = int(input("put the another number"))
        print("we  put to your  account", amount, )
    print("thank you for using our ATM")
