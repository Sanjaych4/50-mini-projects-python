# Day 15: A scientific calculator

import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def power(x, y):
    return x ** y

def square(x):
    return x ** 2

def cube(x):
    return x ** 3

def sin(x):
    return math.sin(x)

def cos(x):
    return math.cos(x)

def tan(x):
    return math.tan(x)

def arcsin(x):
    return math.asin(x)

def arccos(x):
    return math.acos(x)

def arctan(x):
    return math.atan(x)

def log10(x):
    return math.log10(x)

def ln(x):
    return math.log(x)

def sqrt(x):
    return math.sqrt(x)

print("Welcome to the Scientific Calculator!")

while True:
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square Root")
    print("7. Square")
    print("8. Cube")
    print("9. Sine")
    print("10. Cosine")
    print("11. Tangent")
    print("12. Arcsine")
    print("13. Arccosine")
    print("14. Arctangent")
    print("15. Logarithm (base 10)")
    print("16. Natural Logarithm")
    print("0. Exit")

    choice = input("Enter choice (0-16): ")

    if choice == '0':
        break

    if choice in ('1', '2', '3', '4', '5'):
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))

    if choice == '1':
        print( x, "+", y, "=", add(x, y))

    elif choice == '2':
        print( x, "-", y, "=", subtract(x, y))

    elif choice == '3':
        print( x, "*", y, "=", multiply(x, y))

    elif choice == '4':
        print( x, "/", y, "=", divide(x, y))

    elif choice == '5':
        print( x, "**", y, "=", power(x, y))

    elif choice == '6':
        x = float(input("Enter a number: "))
        print("Square root of", x, "=", sqrt(x))

    elif choice == '7':
        x = float(input("Enter a number: "))
        print("Square of", x, "=", square(x))

    elif choice == '8':
        x = float(input("Enter a number: "))
        print("Cube of", x, "=", cube(x))

    elif choice == '9':
        x = float(input("Enter an angle in radians: "))
        print("Sine of", x, "=", sin(x))

    elif choice == '10':
        x = float(input("Enter an angle in radians: "))
        print("Cosine of", x, "=", cos(x))

    elif choice == '11':
        x = float(input("Enter an angle in radians: "))
        print("Tangent of", x, "=", tan(x))

    elif choice == '12':
        x = float(input("Enter a value between -1 and 1: "))
        print("Arcsine of", x, "=", arcsin(x))

    elif choice == '13':
        x = float(input("Enter a value between -1 and 1: "))
        print("Arccosine of", x, "=", arccos(x))
    elif choice == '14':
        x = float(input("Enter a value: "))
        print("Arctangent of", x, "=", arctan(x))

    elif choice == '15':
        x = float(input("Enter a number: "))
        print("Logarithm (base 10) of", x, "=", log10(x))

    elif choice == '16':
        x = float(input("Enter a number: "))
        print("Natural logarithm of", x, "=", ln(x))

    else:
        print("Invalid input")
