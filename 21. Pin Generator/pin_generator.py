# Day 21: A 4 or 6-digit PIN generator

import random

# prompt the user to choose a PIN length
while True:
    pin_length = input("Choose a PIN length (4 or 6 digits): ")
    if pin_length in ["4", "6"]:
        pin_length = int(pin_length)
        break
    else:
        print("Invalid input, please enter 4 or 6.")

# generate a random PIN number of the specified length
pin_number = random.sample(range(10**(pin_length-1), 10**pin_length), 1)[0]

# print the generated PIN number
print(f"Your {pin_length}-digit PIN is: {pin_number}")
