# Day 40: Select a site or sites

import webbrowser
import random
import time

a = int(input("Enter a number between 1 and 5: "))
if a < 1 or a > 5: # to avoid crashing restricted to 1 to 5 tabs only
    print("Invalid input. Please enter a number between 1 and 5.")
else:
    address = ['google.com', 'gmail.com', 'hotstar.com', 'youtube.com', 'wikipedia.com', 'amazon.com']
    for i in range(a):
        no = random.randrange(len(address))
        webbrowser.open_new_tab("http://" + address[no])
        time.sleep(2)
