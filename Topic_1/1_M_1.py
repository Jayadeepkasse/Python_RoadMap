#Write a script that prints a multi-line string. 
print(""" jay
      is 
      Human""")

# Alternatives:
'''Using Escape Characters: An alternative to triple quotes is using escape characters (\n) to manually insert new lines. However, this approach is less readable and harder to maintain, especially for long strings.

Example Using Escape Characters:

print("jay\n      is\n      Human")

While this produces the same output, it's more cumbersome to write and maintain compared to triple quotes.'''

# Text Formatting: 
'''You can further improve the readability by adjusting the formatting to ensure consistent indentation or dynamic content insertion using variables and f-strings.

Example with Dynamic Content:

name = "Jay"
description = "Human"
print(f"""{name}
      is 
      {description}""")
Here, the variables name and description are inserted dynamically, making the script more flexible and reusable for different inputs.'''

# Using Single Quotes: 
"""If you prefer, you can use single quotes (''') instead of double quotes ("_"") to create multi-line strings. Both work the same way in Python, and it’s more about personal preference.

Example with Single Quotes:

print('''jay
      is 
      Human''')
      
This will produce the same output, giving you flexibility in choosing how to write multi-line strings."""

#What You’ve Learned:
"""Core Concept: You’ve learned how to create and print multi-line strings in Python using triple quotes ("_"" or '''). This allows you to format text exactly as you want, with line breaks and indentation preserved.
Learning Concept: You’ve learned how to use the print() function to display multi-line strings and maintain formatting. You’ve also explored the use of escape characters (\n) as an alternative to triple quotes, though it's less clean.
Improvements: You can make the script more dynamic by using variables with f-strings and have flexibility in text formatting. You’ve also learned the option of using single quotes for multi-line strings.
Best Practice:
Use triple quotes for multi-line strings as they are more readable and easier to manage.
For dynamic content insertion, prefer f-strings over concatenating strings or manually adding new lines.
Maintain consistent formatting, especially when dealing with multi-line text, to ensure your output is neat and easy to read."""