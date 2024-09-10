#Write a script that takes user input and prints it.
User_Input=input("Input_Value :")
print(f"This is User's Input : {User_Input}")


#Alternatives:
"""  Handle Empty Input: You can add a check to handle cases where the user doesn't enter anything:

User_Input = input("Input_Value: ")
if User_Input:
    print(f"This is User's Input: {User_Input}")
else:
    print("No input provided.")
    
Strip Whitespace: If you want to remove leading and trailing whitespace from the input:

User_Input = input("Input_Value: ").strip()
print(f"This is User's Input: {User_Input}")

Experimenting with these variations can help you handle different user input scenarios and improve your understanding of input handling in Python."""

"""What You’ve Learned:
You used input(): This function gets user input from the console.
You displayed user input: The print() function with an f-string shows the user's input in a formatted message.
"""