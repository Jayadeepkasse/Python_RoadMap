#Write a script that calculates the factorial of a number.
def facto(n):
    fact_num=1
    for i in range(1,n+1):
        fact_num=fact_num*i
    return fact_num

try:
    n=int(input("Enter the number to do factorial :"))
    if n<0:
        print("Enter Positive values")
    else:
        print(f"This is the Factorial({n}) value :",facto(n))
except ValueError:
    print("Entered Invalid Values")

    # Alternatives:
"""Allowing for Factorial of 0: By definition, the factorial of 0 is 1 (i.e., 0! = 1).
    You can improve the code by handling this specific case.

Example Code with Factorial of 0:

def facto(n):
    fact_num = 1
    for i in range(1, n + 1):
        fact_num = fact_num * i
    return fact_num

try:
    n = int(input("Enter the number to do factorial: "))
    if n < 0:
        print("Enter Positive values")
    elif n == 0:
        print(f"Factorial(0) is 1")
    else:
        print(f"This is the Factorial({n}) value: ", facto(n))
except ValueError:
    print("Entered Invalid Values")
This allows the program to handle 0! correctly."""

# Using Recursion: 
"""An alternative to using a loop is to calculate the factorial using recursion, where the function calls itself until it reaches the base case (n == 1)
Example with Recursion:

def facto(n):
    if n == 1:
        return 1
    else:
        return n * facto(n - 1)

try:
    n = int(input("Enter the number to do factorial: "))
    if n <= 0:
        print("Enter Positive values")
    else:
        print(f"This is the Factorial({n}) value: ", facto(n))
except ValueError:
    print("Entered Invalid Values")

This recursive version computes the factorial by repeatedly calling facto(n-1)."""

#Factorial Using math Library: 
"""Python provides a built-in method for calculating the factorial using the math library. 
This method is optimized and may be preferred for larger values of n.

Example Using math.factorial():

import math

try:
    n = int(input("Enter the number to do factorial: "))
    if n < 0:
        print("Enter Positive values")
    else:
        print(f"This is the Factorial({n}) value: ", math.factorial(n))
except ValueError:
    print("Entered Invalid Values")

This is a more efficient and compact way to compute the factorial."""

# What You’ve Learned:
"""Core Concept: You’ve learned how to calculate the factorial of a number using iteration. The factorial is the product of all integers from 1 to n.
Learning Concept: You’ve seen how to handle user input using try-except blocks to prevent invalid inputs from causing crashes, and how to validate that the input is a positive number.
Improvements: You can use recursive methods or built-in library functions (math.factorial) to calculate the factorial more efficiently. Additionally, handling the case of 0! ensures correctness.
"""
# Best Practice:
"""Validate input: Ensure the user provides positive integers for factorial calculations.
Consider recursion: For educational purposes or smaller values, recursion offers a clear way to understand the factorial process.
Use built-in functions: When performance is critical or for large values of n, use optimized built-in methods like math.factorial()."""