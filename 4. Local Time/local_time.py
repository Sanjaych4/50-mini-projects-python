# Day 4: A localized digital clock (time, date, day of week)

from datetime import datetime
import pytz
import time

# Taking the Indian Standard Timezone as the default timezone
local_timezone = pytz.timezone('Asia/Kolkata')

while True:
    # get the current time in the local timezone
    current_time = datetime.now(local_timezone)

    # format the time as HH:MM:SS AM/PM
    formatted_time = current_time.strftime("%I:%M:%S %p")

    # clears the screen and print the formatted time
    print("\033c" + formatted_time)

    # updates on every second
    time.sleep(1)
