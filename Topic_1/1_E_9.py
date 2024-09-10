#Write a script that prints the square of a number.
x=4
print(f"Square of the Number({x}) is ",x**2)

#Best Practice Problem:
"""def Square_Number(a):
    return a**2
  
try:
    x=int(input("Enter Input Value :"))
    print(f"Square of the Number({x}) is ",Square_Number(x))
except:
    print("Value You Entered is not Correct")"""

# Alternatives:
""" Taking Input from the User: You can modify the code to take the number as input from the user instead of hardcoding the value. This way, it becomes more flexible.

Improved Code Example:
x = int(input("Enter a number: "))
print(f"Square of the Number({x}) is {x**2}")

Here, the input() function allows the user to provide a number at runtime, and int() converts the input to an integer. 
This is a more dynamic and interactive approach, making the script useful for different values.

Error Handling: It’s good practice to include basic error handling to ensure that the user inputs a valid number. You can wrap the input code in a try-except block to handle exceptions.

Code Example with Error Handling:

try:
    x = int(input("Enter a number: "))
    print(f"Square of the Number({x}) is {x**2}")
except ValueError:
    print("Please enter a valid integer.")
    
This improvement ensures that if the user inputs something other than a valid integer, the program won’t crash and will instead display an appropriate message.

Reusable Function: You could encapsulate the logic inside a function to make the code reusable.

Code Example with Function:

def square_number(x):
    return x**2

x = int(input("Enter a number: "))
print(f"Square of the Number({x}) is {square_number(x)}")
This approach allows you to call square_number() with any number you want, making the code more modular and reusable."""

#What You’ve Learned:
"""Core Concept: You learned how to use basic arithmetic operators in Python to perform exponentiation (square of a number).
Learning Concept: You learned how to format output using f-strings and print results clearly and efficiently.
Improvements: You can enhance the script by allowing user input, adding error handling for invalid inputs, and using functions to make the code modular and reusable."""
#Best Practice:
"""Use input() to make your program interactive rather than hardcoding values.
Always consider error handling (like using try-except) to make your programs robust.
Encapsulate your logic in functions when possible to increase code reusability and maintainability."""
