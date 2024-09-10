#Write a script that prints the first 10 natural numbers.
for x in range(1,11):
    print(x)
    
    
"""What You’ve Learned:
You used a loop: The for loop iterates through a sequence of numbers.
You printed numbers: Each number from 1 to 10 was displayed on a new line.
By running and experimenting with these variations, you can see different ways to achieve the same goal and learn more about Python's capabilities."""

#Alternatives:
"""Using List Comprehension: If you want to create a list of the first 10 natural numbers and print it:
numbers = [x for x in range(1, 11)]
print(numbers)
This will print the numbers as a list: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].

Print in One Line: If you prefer to print all numbers in one line separated by spaces:
print(*range(1, 11))
This will produce the output: 1 2 3 4 5 6 7 8 9 10."""
