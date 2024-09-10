#Write a script that prints the sum of two numbers.
def sum(a,b):
    return a+b

try:
    x,y=int(input("Enter Values of x :")),int(input("Enter Values of y :"))
    print(f"sum of x,y is ",sum(x,y))
except:
    print("Enter Correct Values")
   
#Best Practice Prblm:   
"""def Calculate_sum(nums):
    return sum(nums)
try:
    numbers=list(map(int,input("Enter the Numbers to do sub operation with space :").split(",")))
    #print(numbers)
    print(f"sum of {numbers} is ",sum(numbers))
except:
    print("Enter Correct Values") """
     
# Alternatives:
"""Specify the Type of Exception: It's better practice to specify the type of exception you're handling instead of using a bare except.
In this case, you’re expecting a ValueError when a non-integer input is entered, so the except block should catch that specific error.

Improved Code Example:

def sum(a, b):
    return a + b
try:
    x = int(input("Enter Values of x: "))
    y = int(input("Enter Values of y: "))
    print(f"sum of x, y is {sum(x, y)}")
except ValueError:
    print("Please enter valid integers.")
    
This ensures the code is handling only the expected error and not accidentally catching other exceptions that may be important to address differently."""

# Reusable Functions with Dynamic Inputs: You can extend this script by allowing it to sum multiple numbers dynamically by using a list and a loop.

"""Code Example with Multiple Inputs:

def sum_numbers(numbers):
    return sum(numbers)
try:
    numbers = list(map(int, input("Enter numbers separated by space: ").split()))
    print(f"Sum of the numbers is {sum_numbers(numbers)}")
except ValueError:
    print("Please enter valid integers.")

Here, the user can input multiple numbers, separated by spaces, and the program will sum them all up. This is more flexible and shows how to handle multiple inputs efficiently.
"""
# Handling Edge Cases: You can handle scenarios where the user inputs negative numbers, zero, or very large numbers, ensuring the program behaves as expected.

"""Example Edge Case Handling:

def sum(a, b):
    return a + b
try:
    x = int(input("Enter Values of x (can be negative or zero): "))
    y = int(input("Enter Values of y (can be negative or zero): "))
    print(f"sum of x, y is {sum(x, y)}")
except ValueError:
    print("Please enter valid integers.")

This accounts for the fact that users may input negative numbers or zero, and the program should still function correctly."""
# What You’ve Learned:
"""Core Concept: You now understand how to define functions and perform arithmetic operations in Python. You also understand how to handle user input and return a result using the print() function with f-strings.
Learning Concept: You’ve learned to use error handling (try-except) to manage invalid input gracefully, preventing program crashes.
Improvements: Handling specific exceptions, summing multiple inputs, and ensuring flexibility in input values are key improvements to make the code more robust and flexible."""
#Best Practice:
"""Use specific exception types (like ValueError) in try-except blocks to avoid catching unintended errors.
Extend input flexibility: Allow users to input multiple numbers and sum them up to make the program more dynamic.
Edge Case Handling: Ensure the program works with negative numbers, zero, and large values.
This approach makes your code more efficient, user-friendly, and maintainable, ensuring it can handle a variety of real-world scenarios."""


