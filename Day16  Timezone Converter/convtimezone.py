# Day 16: Timezone Converter

import pytz
import datetime

# Get a list of available timezones
available_timezones = pytz.all_timezones

print("Available timezones:")
for tz in available_timezones:
    print(tz)

# Get user input for the original timezone
orig_tz = input("Enter the original timezone: ")

# Get user input for the target timezone
target_tz = input("Enter the target timezone: ")

# Get the current time in the original timezone
orig_dt = datetime.datetime.now(pytz.timezone(orig_tz))

# Convert the time to the target timezone
target_dt = orig_dt.astimezone(pytz.timezone(target_tz))

# Print the result
print("The time in {} is {}.".format(target_tz, target_dt.strftime("%d-%m-%Y %H:%M:%S %Z%z")))
