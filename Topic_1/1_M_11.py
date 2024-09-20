#Write a script that prints the ASCII value of a character.
def Ascii_Value(x):
    return ord(x)

try:
    s=(input("Enter the value to Print Ascii Value of the char -"))
    if(len(s)!=1):
        raise ValueError("Please Enter Exactly One Char")

    print(f"this is the ASCII Value of '{s}' ->",Ascii_Value(s))
except ValueError as e:
    print(e)


# Alternatives:
"""Handling Non-Printable Characters: ASCII includes non-printable characters (like newline '\n', tab '\t'). 
You can extend the code to handle these characters and explain their ASCII values.

Example:

def Ascii_Value(x):
    return ord(x)

try:
    s = input("Enter the value to print ASCII value of the character: ")
    if len(s) != 1:
        raise ValueError("Please Enter Exactly One Character")
    ascii_value = Ascii_Value(s)
    if ascii_value < 32 or ascii_value == 127:
        print(f"'{s}' is a non-printable ASCII character with value {ascii_value}")
    else:
        print(f"This is the ASCII Value of '{s}' -> {ascii_value}")
except ValueError as e:
    print(e)
This modification handles non-printable ASCII characters by checking their ASCII value range (0-31 and 127)."""

# Extend to Unicode Characters: 
"""ASCII only covers values from 0 to 127, but Unicode expands the character set to include more symbols and characters from other languages. 
Python's ord() can handle Unicode characters as well.

Example with Unicode Support:

def Ascii_Value(x):
    return ord(x)

try:
    s = input("Enter the value to print ASCII/Unicode value: ")
    if len(s) != 1:
        raise ValueError("Please Enter Exactly One Character")
    print(f"The Unicode/ASCII value of '{s}' is {Ascii_Value(s)}")
except ValueError as e:
    print(e)
This version works for both ASCII and Unicode characters."""

# Using chr() for Reverse Operation: 
"""You can also provide the reverse functionality where a number is input, and the corresponding character is returned using the chr() function.

Example with chr():

def char_from_ascii(n):
    return chr(n)

try:
    n = int(input("Enter an ASCII value to get its corresponding character: "))
    if n < 0 or n > 127:
        raise ValueError("Please enter a valid ASCII value (0-127)")
    print(f"The character for ASCII value {n} is '{char_from_ascii(n)}'")
except ValueError as e:
    print(e)
This allows the user to input an ASCII value (0-127), and the corresponding character will be printed."""

# What You’ve Learned:
"""Core Concept: You’ve learned how to convert a character into its ASCII value using the ord() function in Python. 
ASCII values are widely used in text encoding, cryptography, and character manipulations.
Learning Concept: You’ve also seen how to handle input validation, ensuring the user enters exactly one character, and how to handle errors gracefully with try-except.
Improvements: Handling non-printable ASCII characters and expanding the code to include Unicode support gives you a broader perspective. 
Using chr() for the reverse operation (from ASCII to character) is also a valuable technique."""
# Best Practice:
"""Validate input: Ensure that the input is a single character, and handle cases where the user provides more than one character or an empty string.
Handle non-printable characters: Recognize that some ASCII values represent non-printable characters and handle them accordingly.
Use chr() for reverse lookups: When needed, use the chr() function to get the character for a given ASCII or Unicode value."""
