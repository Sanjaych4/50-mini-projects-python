# Day 14: A countdown clock

import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs) #formatiing the integer
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print("Time's up!")

duration = int(input("Enter the duration of the countdown timer (in seconds): "))

countdown(duration)
