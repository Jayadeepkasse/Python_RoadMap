#Write a script that prints the current year.
import datetime
Now=datetime.datetime.now()
print(Now.strftime("%y"))
print(Now.year)

#Alternatives:
"""More Efficient Use of the datetime Module: Instead of calling datetime.datetime.now() and then formatting it with strftime() and year, you can directly use datetime.date.today()
if you only care about the date (and not the time). This is more efficient as it directly provides the current date.

Consolidating Outputs: You could use a single print() statement to format and print both the last two digits of the year and the full year together using Python’s f-strings. This improves readability and reduces code redundancy.

Best Practice – Avoid Redundant Calls: Avoid calling datetime.datetime.now() multiple times if you don't need the full date-time object. Use today() when you only need the date.

Improved Code Example:
import datetime
today = datetime.date.today()
print(f"Year (last two digits): {today.strftime('%y')}, Full Year: {today.year}")
This code is simpler and more efficient, as it avoids retrieving unnecessary data (like time) when you're only interested in the date."""

#What You’ve Learned:
"""Core Concept: You’ve learned how to use Python's datetime module to work with date and time, extract specific components (like the year), and format the output using strftime().
Learning Concept: You now know how to access different parts of a datetime object and output them as needed.
Improvements: By using datetime.date.today() when you don’t need time, and consolidating outputs with f-strings, you make your code cleaner and more efficient.
Best Practice:
Use f-strings for clean and readable output.
Use datetime.date.today() when you don’t need the full datetime object.
Keep your code concise and avoid redundant calls to make it more efficient."""