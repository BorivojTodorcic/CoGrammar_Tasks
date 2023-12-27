"""

Start

Request user to enter their name
Store this value as a variable called name

Request user to enter their age
Store this value as a variable called age

Request user to enter their house number
Store this value as a variable called house_number

Request user to enter their street name
Store this value as a variable called street_name

Print the 4 variables using a f-string

End

"""

name = input("What is your name? ")
age = input("How old are you? ")
house_number = input("What is your house number? ")
street_name = input("What is the name of the street you live on? ")

print(f"This is {name}. He is {age} years old and lives at house number {house_number} on {street_name} Street")