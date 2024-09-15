#Write a script that prints the Fibonacci sequence up to 10 terms.
def Fib_Seq(x):
    a,b=0,1
    Fib_List=[]
    for i in range(x):
        Fib_List.append(a)
        a,b=b,a+b
    return Fib_List

try:
    n=int(input("Enter the Max Terms to Print Fibonacci sequence :"))
    print(f"This is Fibonacci sequence for {n} Terms ",Fib_Seq(n))

except ValueError:
    print("Enter VALID number as Input")



    
# Alternatives:
"""Allowing for Negative or Zero Input: You can improve the script by handling cases where the user enters zero or a negative number,
-as Fibonacci sequences are defined for positive integers.

Example with Validation:

def Fib_Seq(x):
    a, b = 0, 1
    Fib_List = []
    for i in range(x):
        Fib_List.append(a)
        a, b = b, a + b
    return Fib_List

try:
    n = int(input("Enter the Max Terms to Print Fibonacci sequence: "))
    if n <= 0:
        print("Please enter a positive number.")
    else:
        print(f"This is Fibonacci sequence for {n} Terms ", Fib_Seq(n))
except ValueError:
    print("Enter VALID number as Input")

This ensures that the user provides a valid number of terms (greater than 0)."""

# Using Recursion: 
"""An alternative way to generate Fibonacci numbers is by using recursion. 
This is a more elegant (but less efficient) method for smaller sequences.

Example Using Recursion:

def Fib_Seq_Rec(n):
    if n <= 1:
        return n
    else:
        return Fib_Seq_Rec(n-1) + Fib_Seq_Rec(n-2)

try:
    n = int(input("Enter the Max Terms to Print Fibonacci sequence: "))
    if n <= 0:
        print("Please enter a positive number.")
    else:
        Fib_List = [Fib_Seq_Rec(i) for i in range(n)]
        print(f"This is Fibonacci sequence for {n} Terms ", Fib_List)
except ValueError:
    print("Enter VALID number as Input")

This version uses recursion to calculate each term in the Fibonacci sequence."""

# Using Generators: 
"""You can improve the memory efficiency by using a generator instead of appending all values to a list. 
Generators yield values one by one, which is useful when working with larger sequences.

Example with Generator:

def Fib_Gen(x):
    a, b = 0, 1
    for i in range(x):
        yield a
        a, b = b, a + b

try:
    n = int(input("Enter the Max Terms to Print Fibonacci sequence: "))
    if n <= 0:
        print("Please enter a positive number.")
    else:
        Fib_List = list(Fib_Gen(n))
        print(f"This is Fibonacci sequence for {n} Terms ", Fib_List)
except ValueError:
    print("Enter VALID number as Input")

This is more efficient, especially when working with very large Fibonacci sequences."""

# What You’ve Learned:
"""Core Concept: You’ve learned how to generate and print the Fibonacci sequence in Python using loops, and how to calculate subsequent Fibonacci numbers by updating the values of a and b.
Learning Concept: You’ve seen how to handle user input and errors using try-except, and how to format output using f-strings.
Improvements: You can implement recursive solutions or use generators for better memory efficiency. You can also handle edge cases like negative or zero input.
Best Practice:
Use loops for iterative generation: This is efficient and easy to understand for small to medium-sized sequences.
Handle edge cases: Ensure that inputs are positive integers and handle invalid inputs gracefully.
Use generators for large sequences: Generators save memory by yielding values one by one, which is ideal when working with large datasets."""