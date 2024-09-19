#Write a script that finds the maximum of three numbers.
def check_Max(x,y,z):
    return max(x,y,z)

try:
    a=input("Enter Value of 'a' :" )
    b=input("Enter Value of 'b' :" )
    c=input("Enter Value of 'c' :" )
    print(f"This is the largest value of ({a},{b},{c})",check_Max(a,b,c))
except:
    print("Enter valid Input")

# Alternatives:
"""Handling Edge Cases: The script could be enhanced to handle edge cases where two or all three numbers are equal. 
While the max() function already works for these cases, a message explaining that values are equal could provide better feedback.

Example Code with Equal Numbers Handling:

def check_Max(x, y, z):
    if x == y == z:
        return f"All values are equal: {x}"
    return max(x, y, z)

try:
    a = float(input("Enter Value of 'a': "))
    b = float(input("Enter Value of 'b': "))
    c = float(input("Enter Value of 'c': "))
    result = check_Max(a, b, c)
    print(f"This is the largest value of ({a}, {b}, {c})", result)
except ValueError:
    print("Enter valid numeric input")
If the values are equal, this will print:"""


"""All values are equal: 5.5
Allowing Multiple Inputs at Once: You could modify the script to allow the user to enter all three numbers in a single input, separated by spaces. 
This approach simplifies input collection.

Example Code with Multiple Inputs:

def check_Max(x, y, z):
    return max(x, y, z)

try:
    values = list(map(float, input("Enter three values separated by space: ").split()))
    if len(values) != 3:
        print("Please enter exactly three values.")
    else:
        print(f"This is the largest value of ({values[0]}, {values[1]}, {values[2]})", check_Max(*values))
except ValueError:
    print("Enter valid numeric input")
This allows the user to input values like 5.5 8.1 3.2 in a single line."""

# Improved Error Messages: 
"""You can enhance the error messages to be more specific by catching the exact type of invalid input, such as empty inputs or strings.

Example with Specific Error Messages:

def check_Max(x, y, z):
    return max(x, y, z)

try:
    a = float(input("Enter Value of 'a': "))
    b = float(input("Enter Value of 'b': "))
    c = float(input("Enter Value of 'c': "))
    print(f"This is the largest value of ({a}, {b}, {c})", check_Max(a, b, c))
except ValueError as ve:
    print(f"Invalid input: {ve}. Please enter numeric values.")
This would provide more detailed feedback about what went wrong in case of invalid input."""

# What You’ve Learned:
"""Core Concept: You’ve learned how to find the maximum of three numbers using Python’s max() function. 
This is a basic, yet fundamental, operation in programming.
Learning Concept: You’ve seen how to handle user input, convert it to the correct data type (float() for numeric values), and handle invalid input with try-except blocks.
Improvements: By handling equal numbers and using single-line input for multiple values, you make the script more user-friendly and efficient. 
Additionally, providing better error messages makes the code easier to debug and use."""
# Best Practice:
"""Use max() for simplicity: The max() function is built-in and efficient for finding the maximum value among multiple arguments.
Handle invalid inputs gracefully: Use try-except blocks to ensure the program doesn’t crash and gives meaningful feedback.
Consider edge cases: Always account for edge cases, such as when the values are equal, and provide appropriate feedback to the user."""