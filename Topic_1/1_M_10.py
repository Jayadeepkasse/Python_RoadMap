#Write a script that reverses a string.
def reverse_String(x):
    rev_S=str(x[::-1])
    return rev_S

try:
    s=str(input("Enter a String :"))
    print(f"Reversed String is {reverse_String(s)}")
except ValueError as VE:
    print(f"Entered value Error is {VE} , Please Enter Valid Value")


# Alternatives:
"""Handling Non-String Input Gracefully: You can ensure that the user provides a valid string by checking the input type before proceeding to reverse it.

Example Code with Input Validation:

def reverse_String(x):
    if isinstance(x, str):
        return x[::-1]
    else:
        return "Invalid input. Please enter a valid string."

try:
    s = input("Enter a String: ")
    print(f"Reversed String is {reverse_String(s)}")
except Exception as e:
    print(f"An error occurred: {e}")
This code ensures that only valid strings are processed, and if non-string input is provided, it gives feedback."""

# Using a Loop to Reverse the String: 
"""Although slicing is efficient, another way to reverse a string is to use a loop to build the reversed string one character at a time.

Example with a Loop:

def reverse_String(x):
    rev_S = ""
    for char in x:
        rev_S = char + rev_S
    return rev_S

s = input("Enter a String: ")
print(f"Reversed String is {reverse_String(s)}")
This approach builds the reversed string character by character. 
Though less efficient than slicing, it’s useful for educational purposes to understand string manipulation."""

# Using Python’s Built-in reversed() Function: 
"""You can also reverse a string by using Python’s built-in reversed() function, which returns an iterator over the characters of the string.

Example Using reversed():

def reverse_String(x):
    return ''.join(reversed(x))

s = input("Enter a String: ")
print(f"Reversed String is {reverse_String(s)}")
This method uses reversed() to get an iterator, which is then joined back into a string using ''.join()."""

# What You’ve Learned:
"""Core Concept: You’ve learned how to reverse a string using slicing in Python ([::-1]), which is both simple and efficient. 
Slicing is a powerful tool for manipulating sequences in Python.
Learning Concept: You now understand how to handle user input, manipulate strings with slicing, and use a try-except block to handle potential errors.
Improvements: Using input validation ensures that only valid strings are processed. 
You’ve also seen alternative methods such as loops and the reversed() function for reversing strings.
Best Practice:
Use slicing: Slicing ([::-1]) is the most efficient way to reverse a string in Python. It’s concise and performs well.
Validate input: Always validate user input to ensure that the program handles non-string inputs gracefully.
Use reversed() for iterator-based reversal: When working with very large sequences, using reversed() with ''.join() can be a more memory-efficient approach.
By understanding these concepts and best practices,
you'll have a strong foundation for string manipulation, which is essential in data processing and text handling in Machine Learning and AI tasks."""