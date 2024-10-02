import random
import string
def password_generator(minimum_length,numbers = True,special_characters = True) :
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    character = letters
    if numbers:
        character += digits
    if special_characters :
        character += special

    pwd= ""
    has_numbers = False
    has_special = False
    meet_criteria = False

    while not meet_criteria or len(pwd) < minimum_length:
        new_char = random.choice(character)
        pwd += new_char

        if new_char in digits:
            has_numbers = True
        elif new_char in special:
            has_special = True
        

        meet_criteria = True
        if numbers :
            meet_criteria = has_numbers
        if special_characters:
            meet_criteria = meet_criteria and has_special

    return pwd


min_length = int(input("Enter the minimum length of the password: "))
has_special = input("Do you want special character (y/n) :").lower() == "y"
has_numbers = input("Do you want numbers (y/n) : ").lower() == "y"
pwd = password_generator(min_length,has_numbers,has_special)
print("Generated password is : ",pwd)      