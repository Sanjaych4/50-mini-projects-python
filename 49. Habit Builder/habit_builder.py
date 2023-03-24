# Day 49: A habit builder app (notifies to drink water, to stand up every 30 minutes, etc.)
# `pip install plyer` before running this program
# works only on windows

from plyer import notification
import time

def drink_water():
    notification.notify(
    title="Drink Water",
    message="Remember to drink water every hour!",
    app_name="Habit Builder",
    timeout=10
    )
def stand_up():
    notification.notify(
    title="Stand Up",
    message="Remember to stand up every 30 minutes!",
    app_name="Habit Builder",
    timeout=10
    )

def main():
    while True:
        drink_water()
        time.sleep(3600)
        stand_up()
        time.sleep(1800)

def main():
    while True:
        drink_water()
        time.sleep(3600)

if __name__ == "__main__":
    main()
