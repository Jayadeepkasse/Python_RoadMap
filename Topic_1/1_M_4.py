#Write a script that takes two inputs and swaps their values.
def Swap_Vals(a,b):
    return b,a

try:
    i1=(input("Enter First Input :"))
    i2=(input("Enter second Input :"))
    print(f"Swaped Values of First Input('{i1}') and Second Input('{i2}')are ",Swap_Vals(i1,i2)[0],",",Swap_Vals(i1,i2)[1])
except ValueError:
    print("Enter Valid inputs")


# Alternatives:
"""Simplify Output: Instead of calling Swap_Vals(i1, i2) twice, you can store the swapped values in variables and print them directly. 
This makes the code more efficient and cleaner.
Improved Code Example:

def Swap_Vals(a, b):
    return b, a

try:
    i1 = input("Enter First Input: ")
    i2 = input("Enter Second Input: ")
    swapped_i1, swapped_i2 = Swap_Vals(i1, i2)
    print(f"Swapped Values of First Input ('{i1}') and Second Input ('{i2}') are {swapped_i1}, {swapped_i2}")
except ValueError:
    print("Enter Valid Inputs")

This avoids calling the Swap_Vals() function twice and improves the code’s performance and readability."""

# Allowing Numerical Input: 
"""You can expand the program to handle both string and numeric inputs by checking the type of the input and handling each accordingly. 
This way, the program can be more flexible.
Code Example with Numeric Handling:

def Swap_Vals(a, b):
    return b, a
try:
    i1 = input("Enter First Input: ")
    i2 = input("Enter Second Input: ")

    # Check if inputs can be converted to numbers
    try:
        i1 = float(i1)
        i2 = float(i2)
    except ValueError:
        pass  # If inputs are not numbers, keep them as strings

    swapped_i1, swapped_i2 = Swap_Vals(i1, i2)
    print(f"Swapped Values are {swapped_i1}, {swapped_i2}")
except Exception as e:
    print(f"An error occurred: {e}")

This modification allows the program to handle both numeric and string inputs seamlessly."""

# Edge Case Handling: 
"""You can handle edge cases where the user inputs empty strings or inputs the same value for both inputs. 
These cases can be handled by adding conditions to check for such scenarios.
Example for Edge Cases:

if i1 == i2:
    print("Both inputs are the same, no swap needed.")
elif i1 == "" or i2 == "":
    print("Input cannot be empty.")
else:
    swapped_i1, swapped_i2 = Swap_Vals(i1, i2)
    print(f"Swapped Values are {swapped_i1}, {swapped_i2}")

This checks for identical inputs or empty inputs and provides an appropriate message."""
# What You’ve Learned:
"""Core Concept: You’ve learned how to swap values in Python using simple variable assignment and returning values in reverse order. Python’s ability to handle multiple return values makes swapping very easy.
Learning Concept: You’ve seen how to take input from users, use a function to swap the values, and print the result using f-strings for clear and formatted output.
Improvements: Storing swapped values before printing improves efficiency, and handling both numeric and string inputs makes the code more flexible and robust.
Best Practice:
Avoid redundant function calls by storing return values in variables before using them.
Handle both string and numeric inputs for more versatility in your script.
Check for edge cases, such as empty inputs or identical values, to make the program more user-friendly."""
