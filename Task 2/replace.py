"""
Practical Task 2 - String manipulation
"""


my_sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog."

# Removed the "!" and replaced it with a space.
print(my_sentence.replace("!", " "))

# Capitalised the string following the manipulation from the code above.
print(my_sentence.replace("!"," ").upper())

# Reversed the string following the manipulation from the code above.
print(my_sentence.replace("!"," ").upper()[::-1])

