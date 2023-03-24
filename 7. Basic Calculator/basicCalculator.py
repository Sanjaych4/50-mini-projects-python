# Day 7: A basic calculator

#function to add two numbers
def add(x, y):
    return x + y

#function to subtract two numbers
def subtract(x, y):
    return x - y

#function to multiply two numbers
def multiply(x, y):
    return x * y

#function to divide two numbers
def divide(x, y):
    return x / y

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

#Take input from the user
choice = input("Enter choice (1/2/3/4): ")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == '1':
    print("You have selected Addition")
    print(num1,"+",num2,"=", add(num1,num2))

elif choice == '2':
    print("You have selected Substraction")
    print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == '3':
    print("You have selected Multiplication")
    print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == '4':
    print("You have selected Division")
    print(num1,"/",num2,"=", divide(num1,num2))
else:
    print("Invalid input")
