# Day 5: Measurement calculator (weight, distance, area, volume, etc.)

# Define conversion factors (found a json file online lol, that helped me to write half of the program easily.)
weight_conv = {
    "lb": 0.453592, # pounds to kilograms
    "kg": 1.0, # kilograms to kilograms
    "g": 0.001, # grams to kilograms
    "oz": 0.0283495 # ounces to kilograms
}

distance_conv = {
    "km": 1000.0, # kilometers to meters
    "m": 1.0, # meters to meters
    "cm": 0.01, # centimeters to meters
    "mm": 0.001, # millimeters to meters
    "mi": 1609.34, # miles to meters
    "yd": 0.9144, # yards to meters
    "ft": 0.3048, # feet to meters
    "in": 0.0254 # inches to meters
}

area_conv = {
    "km2": 1000000.0, # square kilometers to square meters
    "m2": 1.0, # square meters to square meters
    "cm2": 0.0001, # square centimeters to square meters
    "mm2": 0.000001, # square millimeters to square meters
    "ha": 10000.0, # hectares to square meters
    "ac": 4046.86, # acres to square meters
    "mi2": 2589988.11, # square miles to square meters
    "yd2": 0.836127, # square yards to square meters
    "ft2": 0.092903, # square feet to square meters
    "in2": 0.00064516 # square inches to square meters
}

volume_conv = {
    "m3": 1.0, # cubic meters to cubic meters
    "l": 0.001, # liters to cubic meters
    "ml": 0.000001, # milliliters to cubic meters
    "gal": 0.00378541, # gallons to cubic meters
    "qt": 0.000946353, # quarts to cubic meters
    "pt": 0.000473176, # pints to cubic meters
    "c": 0.000236588, # cups to cubic meters
    "fl oz": 0.0000295735 # fluid ounces to cubic meters
}

# Define function to convert measurement units
def convert(value, unit_from, unit_to, conversion_dict):
    value_m = value * conversion_dict[unit_from]
    value_conv = value_m / conversion_dict[unit_to]
    return value_conv

# Main program
while True:
    print("Measurement Calculator")
    print("---------------------")
    print("1. Weight")
    print("2. Distance")
    print("3. Area")
    print("4. Volume")
    print("5. Exit")
    choice = int(input("Enter your choice (1-5): "))
    if choice == 1:
        value = float(input("Enter weight: "))
        unit_from = input("Enter unit from: ")
        unit_to = input("Enter unit to: ")
        result = convert(value, unit_from, unit_to, weight_conv)
        print(value, unit_from, "is equal to", result, unit_to)
    elif choice == 2:
        value = float(input("Enter distance: "))
        unit_from = input("Enter unit from: ")
        unit_to = input("Enter unit to: ")
        result = convert(value, unit_from, unit_to, distance_conv)
        print(value, unit_from, "is equal to", result, unit_to)
    elif choice == 3:
        value = float(input("Enter area: "))
        unit_from = input("Enter unit from: ")
        unit_to = input("Enter unit to: ")
        result = convert(value, unit_from, unit_to, area_conv)
        print(value, unit_from, "is equal to", result, unit_to)
    elif choice == 4:
        value = float(input("Enter volume: "))
        unit_from = input("Enter unit from: ")
        unit_to = input("Enter unit to: ")
        result = convert(value, unit_from, unit_to, volume_conv)
        print(value, unit_from, "is equal to", result, unit_to)
    elif choice == 5:
        print("See you Later!")
        break
    else:
        print("Invalid choice. Please try again.")

#See you tommorrow :)
