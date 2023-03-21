# Day 20: Event notifier (stores all your events and notifies (say) 30 minutes before)

# Install the Win10toast module before running this program 
#`pip install win10toast` copy and paste this terminal to install the win10toast package
# note: this program only works on windows 10 or above, won't work on MAC OS


from win10toast import ToastNotifier
import datetime


toaster = ToastNotifier()

event_name = input("Enter the event name: ")
event_time = input("Enter the event time in format 'DD-MM-YYYY HH:MM:SS': ")

event_time = datetime.datetime.strptime(event_time, '%d-%m-%Y %H:%M:%S')


notification_time = event_time - datetime.timedelta(minutes=30)


while datetime.datetime.now() < notification_time:
    pass

#send the notification
toaster.show_toast("Event Notifier", f"{event_name} in 30 minutes", duration=10)
