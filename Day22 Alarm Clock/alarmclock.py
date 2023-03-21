# Day 22: An alarm clock

import datetime
import time
import winsound

# Set the alarm time
alarm_time = input("Enter the time in 'HH:MM:SS AM/PM' format: ")

# Convert the alarm time to datetime object
alarm_time = datetime.datetime.strptime(alarm_time, '%I:%M:%S %p')

# Run the loop until the alarm time is reached
while True:
    # Get the current time
    current_time = datetime.datetime.now().strftime("%I:%M:%S %p")

    # Print the current time
    print("Current Time:", current_time)

    # Check if the current time matches the alarm time
    if current_time == alarm_time.strftime("%I:%M:%S %p"):
        print("Time to Wake Up!")
        # Play the alarm sound
        winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
        break

    # Wait for one second
    time.sleep(1)
