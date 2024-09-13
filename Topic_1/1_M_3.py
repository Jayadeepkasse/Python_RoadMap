#Write a script that calculates the area of a rectangle using length and width
def Cal_Area(Len,Wid):
    return (Len*Wid)
try:
    l=float(input("Enter Length of Rectangle :"))
    w=float(input("Enter Width of Rectangle "))
    print(f"Area of Rectangle with length({l}) and Width({w}) is ",Cal_Area(l,w))
except ValueError:
    print("Enter Valid Length and Width")


# What You’ve Learned:
"""Core Concept: You’ve learned how to calculate the area of a rectangle using a simple formula (length × width) and a function to encapsulate the calculation.
Learning Concept: You’ve seen how to handle user input using float() to accept decimal values, and how to handle invalid inputs using a try-except block for error handling.
Improvements: Adding validation for positive values, using default parameters for flexibility, and providing detailed error messages all help improve the script’s robustness and usability.
"""
# Best Practice:
"""Validate inputs: Ensure that length and width are positive numbers before performing calculations.
Use float(): Allow both integer and decimal inputs for greater flexibility.
Handle errors gracefully: Provide clear feedback when the user enters invalid data, so the program remains user-friendly and robust.
"""