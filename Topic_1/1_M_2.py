#Write a script that prints the even numbers between 1 and 50.
def Even_nums(a,b):
    numbers=[x for x in range(a,b) if x%2==0]
    return numbers

try:
    x=int(input("Enter MIN Range :"))
    y=int(input("Enter MIN Range :"))
    print(f"Even Numbers B/W {x} and {y} are \n",Even_nums(x,y))
except ValueError:
    print("enter Valid values")



# Alternatives:
"""Flexible Input Validation: You can modify the input handling to allow for a check that ensures the minimum value (x) is smaller than the maximum value (y). This would prevent scenarios where the user accidentally provides the maximum value first.

Code Example with Input Validation:


def Even_nums(a, b):
    numbers = [x for x in range(a, b) if x % 2 == 0]
    return numbers
try:
    x = int(input("Enter MIN Range: "))
    y = int(input("Enter MAX Range: "))
    if x >= y:
        print("Please ensure the MIN value is smaller than the MAX value.")
    else:
        print(f"Even Numbers B/W {x} and {y} are \n", Even_nums(x, y))
except ValueError:
    print("Enter valid values")

This improvement adds a basic validation to ensure the user provides a valid range, making the script more user-friendly."""

# Allowing Custom Step Sizes: 
"""You can allow the user to specify a custom step size (in this case, 2 for even numbers) instead of checking for even numbers with % 2 == 0.
Code Example with Custom Step:

def Even_nums(a, b, step=2):
    return list(range(a, b, step))
try:
    x = int(input("Enter MIN Range: "))
    y = int(input("Enter MAX Range: "))
    print(f"Even Numbers B/W {x} and {y} are \n", Even_nums(x, y))
except ValueError:
    print("Enter valid values")
This code removes the need for filtering even numbers explicitly and uses a step of 2 to only include even numbers in the range."""

#Edge Case Handling: 
"""Handle edge cases where the user inputs values that result in no even numbers being printed. For example, if x = 1 and y = 2, the output should indicate that no even numbers were found.
Example:

if len(Even_nums(x, y)) == 0:
    print("No even numbers in the given range.")"""

#What You’ve Learned:
"""Core Concept: You’ve learned how to use list comprehension to generate a list of even numbers, and how to work with the range() function to specify numerical ranges.
Learning Concept: You now understand how to take user input, handle errors using try-except, and format output using f-strings for better readability.
Improvements: Input validation ensures that the minimum value is smaller than the maximum, and custom step sizes or error messages help make the script more flexible and user-friendly."""
#Best Practice:
"""Use list comprehension for concise and readable list generation.
Handle invalid inputs and edge cases gracefully with try-except and custom messages.
Ensure your input is properly validated to avoid logical errors in the range.
These practices improve the usability and robustness of your script, making it more versatile and easier to maintain."""