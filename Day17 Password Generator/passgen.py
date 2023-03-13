# Day 17: A password generator

import random
import string

def generate_password(length):
    """Generate a random password of the specified length."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

#Prompt the user for the password length
password_length = int(input("How many characters do you want in your password? ")) #Takes the length of the password from the user

#Generate the password
password = generate_password(password_length)

#Print the password
print("Your password is:", password)
