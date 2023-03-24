# Day 26: Expense tracker

import datetime

# Define a dictionary to store the expenses
expenses = {}

# Define a function to add expenses
def add_expense():
    name = input("Enter the name of the expense: ")
    amount = float(input("Enter the amount of the expense in rupees: "))
    date = datetime.date.today().strftime("%Y-%m-%d")
    if date in expenses:
        expenses[date].append((name, amount))
    else:
        expenses[date] = [(name, amount)]
    print("Expense added successfully.")

# Define a function to view expenses
def view_expenses():
    total = 0
    for date, items in expenses.items():
        print(date)
        for item in items:
            print("  ", item[0], ": ₹", item[1])
            total += item[1]
    print("Total expenses: ₹", total)


# Define a main function to run the program
def main():
    while True:
        print("Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        choice = int(input("Enter your choice (1-3): "))
        if choice == 1:
            add_expense()
        elif choice == 2:
            view_expenses()
        elif choice == 3:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
