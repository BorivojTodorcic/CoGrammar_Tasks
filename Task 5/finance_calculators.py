"""
This is an example of a python program showing if-elif-else statements.
The user selects between an investment or bonds calculator and then inputs various financial information.
If they select the investment calculator, the program outputs their investment earnings
If they select the bonds calculator, the program outputs their monthly home repayments
"""


import math


print("""
Investment - To calculate the amount of interest you'll earn on your investment
Bond - To calculate the amount you'll have to pay on a home loan
""")


calculator_option = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()


if calculator_option == "investment":
    print("\nInvestment Calculator Selected:")
    
    principal_amount = float(input("Please enter the amount of money that you are depositing: £"))
    interest_rate = float(input("Please enter the interest rate: "))
    years = int(input("Please enter the number of years would you like to invest your money: "))
    interest = input('Would you like to use a "simple" or "compound" interest rate calculator?: ').lower()
    
    if interest == "simple":
        total_amount = principal_amount * (1 + ((interest_rate / 100) * years))
        rounded_total = round(total_amount, 2)
        print(f"You will have a total of £{rounded_total}")
    elif interest == "compound":
        total_amount = principal_amount * math.pow((1 + (interest_rate / 100)), years)
        rounded_total = round(total_amount, 2)
        print(f"You will have a total of £{rounded_total}")
    else:
        print("You have not selected a valid option.\nPlease restart the program and try again.")

elif calculator_option == "bond":
    print("\nBond Calculator Selected:")

    house_value = float(input("Please enter the value of the house: £"))
    interest_rate = float(input("Please enter the interest rate: "))
    num_months = int(input("Please enter the number of months you plan to take to repay the bond: "))

    repayment = (((interest_rate / 100) / 12) * house_value) / (1 - (1 + ((interest_rate / 100) / 12)) ** (-num_months))
    rounded_total = round(repayment, 2)
    print(f"Your monthly repayments will be £{rounded_total}")
else:
    print("You have not selected a valid option.\nPlease restart the program and try again.")
