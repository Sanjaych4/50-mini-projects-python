# Day 19: To-Do tracker (manage to-do items)

import datetime
import time

class ToDoItem:

    def __init__(self, task, due_date):
        self.task = task
        self.due_date = datetime.datetime.strptime(due_date, '%d-%m-%Y').date()

    def __str__(self):
        return f'{self.task} (due on {self.due_date})'

class ToDoTracker:

    def __init__(self):
        self.to_do_list = []

    def add_to_do_item(self, task, due_date):
        to_do_item = ToDoItem(task, due_date)
        self.to_do_list.append(to_do_item)
        print(f'Added to-do item: {to_do_item}')

    def remove_to_do_item(self, index):
        if index < 0 or index >= len(self.to_do_list):
            print(f'Error: Invalid index {index}')
            return
        to_do_item = self.to_do_list.pop(index)
        print(f'Removed to-do item: {to_do_item}')

    def print_to_do_list(self):
        """Print the current list of to-do items."""
        print('To-Do List:')
        for i, to_do_item in enumerate(self.to_do_list):
            print(f'{i}. {to_do_item}')

    def check_due_dates(self):
        today = datetime.date.today()
        due_today = [to_do_item for to_do_item in self.to_do_list if to_do_item.due_date == today]
        if due_today:
            print('Reminder: The following to-do items are due today:')
            for to_do_item in due_today:
                print(f'- {to_do_item}')

    def run(self):
        while True:
            command = input('\nEnter a command (add, remove, print, check, quit): ').strip().lower()
            if command == 'add':
                task = input('Enter the task: ')
                due_date = input('Enter the due date (DD-MKM-YYYY): ')
                self.add_to_do_item(task, due_date)
            elif command == 'remove':
                index = int(input('Enter the index of the to-do item to remove: '))
                self.remove_to_do_item(index)
            elif command == 'print':
                self.print_to_do_list()
            elif command == 'check':
                self.check_due_dates()
            elif command == 'quit':
                break
            else:
                print('Error: Invalid command')

        print('Goodbye!')

to_do_tracker = ToDoTracker()
to_do_tracker.run()

