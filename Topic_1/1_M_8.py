#Write a script that checks if a number is prime.
def Is_Not_Prime(x):
    if(x<=1):
        return True
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return True
    return False

try:
    n=int(input("Enter Number to Check Prime Number or not :"))
    if(Is_Not_Prime(n)):
        print(f"Entered value-{n} is not a prime number")
    else:
        print(f"Entered value-{n} is a prime number")
except ValueError:
    print("Enter Valid Input")

# Alternatives:
"""Checking for Edge Cases: You can handle edge cases, such as n = 1, n = 0, or negative numbers, 
by returning True for all numbers less than or equal to 1, which are not prime.

Example with Edge Cases:

def Is_Not_Prime(x):
    if x <= 1:
        return True
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return True
    return False

try:
    n = int(input("Enter Number to Check Prime Number or not: "))
    if Is_Not_Prime(n):
        print(f"Entered value-{n} is not a prime number")
    else:
        print(f"Entered value-{n} is a prime number")
except ValueError:
    print("Enter Valid Input")
This ensures that any number less than or equal to 1 is treated as not prime."""

# Improve User Feedback: 
"""You can provide more specific feedback based on the number entered. 
For instance, if the number is less than or equal to 1, you can print a message explaining that primes are only greater than 1.

Example with Better Feedback:

def Is_Not_Prime(x):
    if x <= 1:
        return True
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return True
    return False

try:
    n = int(input("Enter Number to Check Prime Number or not: "))
    if n <= 1:
        print(f"Entered value-{n} is not prime, as prime numbers are greater than 1.")
    elif Is_Not_Prime(n):
        print(f"Entered value-{n} is not a prime number")
    else:
        print(f"Entered value-{n} is a prime number")
except ValueError:
    print("Enter Valid Input")
This clarifies why certain inputs are not considered prime."""

# What You’ve Learned:
"""Core Concept: 
You’ve learned how to check if a number is prime by testing divisibility up to the square root of the number. 
This optimization ensures that the algorithm runs efficiently.
Learning Concept: You’ve seen how to handle user input, validate the number, and use conditionals to provide meaningful output.
Improvements: Handling edge cases like numbers less than or equal to 1, providing better user feedback, and using optimized checks for divisibility improve the robustness of the code.
"""
# Best Practice:
"""Optimize the prime check: By only checking divisibility up to the square root of the number, you reduce the number of calculations significantly.
Provide clear feedback: When dealing with edge cases like non-prime numbers (0, 1), make sure to explain why these numbers are not considered prime.
Handle input gracefully: Use try-except blocks to handle invalid inputs and prevent crashes."""
