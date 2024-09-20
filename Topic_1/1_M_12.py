#Write a script that converts kilometers to miles.
def convert_KilotoMiles(k):
    return (k*0.6213)

try:
    kilometer=float(input("Enter the Kilometers to see in Miles ->"))
    print(f"Here is the Miles for {kilometer} Kilometers->",round(convert_KilotoMiles(kilometer),3)," Miles")
except ValueError:
    print('Enter Valid Values')

# Alternatives:
"""Allow for Negative and Zero Input: 
You may want to handle cases where the user enters a negative or zero value. 
Distances can't be negative in real-world contexts, so providing feedback for such input would improve the program.

Example Code with Input Validation:

def convert_KilotoMiles(k):
    return k * 0.6213

try:
    kilometer = float(input("Enter the Kilometers to see in Miles: "))
    if kilometer < 0:
        print("Distance cannot be negative. Please enter a positive value.")
    else:
        print(f"Here are the miles for {kilometer} kilometers -> {round(convert_KilotoMiles(kilometer), 3)} miles")
except ValueError:
    print("Enter valid numeric values")
This code checks if the input is negative and prompts the user to enter a positive value."""

# Improving Precision: 
"""You can use a more precise conversion factor (0.621371) instead of 0.6213 for more accurate conversions.

Example with Improved Precision:

def convert_KilotoMiles(k):
    return k * 0.621371

try:
    kilometer = float(input("Enter the Kilometers to see in Miles: "))
    print(f"Here are the miles for {kilometer} kilometers -> {round(convert_KilotoMiles(kilometer), 5)} miles")
except ValueError:
    print("Enter valid numeric values")
Here, the result is rounded to five decimal places to capture higher precision, which is useful in scientific calculations."""

# Converting Back from Miles to Kilometers: 
"""You can extend the functionality to allow users to convert miles back to kilometers by providing an option in the script.

Example with Two-Way Conversion:

def convert_KilotoMiles(k):
    return k * 0.621371

def convert_MilesToKilo(m):
    return m / 0.621371

try:
    choice = input("Convert (1) Kilometers to Miles or (2) Miles to Kilometers: ")
    if choice == '1':
        kilometer = float(input("Enter the Kilometers: "))
        print(f"Here are the miles for {kilometer} kilometers -> {round(convert_KilotoMiles(kilometer), 3)} miles")
    elif choice == '2':
        miles = float(input("Enter the Miles: "))
        print(f"Here are the kilometers for {miles} miles -> {round(convert_MilesToKilo(miles), 3)} kilometers")
    else:
        print("Invalid choice. Please enter 1 or 2.")
except ValueError:
    print("Enter valid numeric values")
This allows the user to choose between converting kilometers to miles or miles to kilometers."""

# What You’ve Learned:
"""Core Concept: 
You’ve learned how to convert kilometers to miles using a simple conversion factor. 
This is a basic concept used in many real-world applications involving distance measurement.
Learning Concept: 
You’ve seen how to use Python’s float() to handle numeric input, apply the round() function for better precision, and handle invalid input with try-except.
Improvements: Handling negative values, improving precision, and adding functionality to convert miles back to kilometers makes the script more robust and user-friendly.
Best Practice:
Use precise conversion factors: Using a more accurate factor (0.621371) improves the precision of the results, especially in scientific or engineering contexts.
Validate user input: Ensure that the input is a positive numeric value and handle invalid input gracefully with informative error messages.
Extend functionality: Consider providing options for two-way conversions to make your script more versatile."""