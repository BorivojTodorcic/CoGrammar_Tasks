"""
Practical Task 1
"""

# Requests user input for their age
age = int(input("How old are you?: "))


# Prints various statements based on the user input value to the code above.
if age > 100:
    print("Sorry, you're dead.")
elif age >= 65:
    print("Enjoy your retirement!")
elif age == 21:
    print("Congrats on your 21st!")
elif age < 13:
    print("You qualify for the kiddie discount.")
else:
    print("Age is but a number.")

