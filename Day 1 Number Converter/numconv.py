# Day 1: A number converter (binary, octal, hexadecimal, custom base)

def convert_number():
    # Get the number to convert and the base it's in
    num = int(input("Enter a number: "))
    base = int(input("Enter the base of the number (2 for binary, 8 for octal, 10 for decimal, 16 for hexadecimal, or a custom base): "))

    # Convert the number to decimal (if it's not already in decimal)
    if base != 10:
        num = int(str(num), base)

    # Get the desired base for the output
    output_base = int(input("Enter the desired output base (2 for binary, 8 for octal, 10 for decimal, 16 for hexadecimal, or a custom base): "))

    # Convert the number to the desired base
    if output_base == 2:
        result = bin(num)[2:]
    elif output_base == 8:
        result = oct(num)[2:]
    elif output_base == 10:
        result = str(num)
    elif output_base == 16:
        result = hex(num)[2:]
    else:
        result = ""

        while num > 0:
            digit = num % output_base
            result = str(digit) + result
            num = num // output_base

    # result
    print("Result:", result)


#the function
convert_number()
