#Write a script that prints the current date and time.
import datetime
current_date_time = datetime.datetime.now()
# Print the raw date and time
print("Current date and time:", current_date_time)

# Print individual components of the date and time
print("Year:", current_date_time.year)
print("Month (numeric):", current_date_time.month)
print("Day of the month:", current_date_time.day)
print("Hour (24-hour format):", current_date_time.hour)
print("Minute:", current_date_time.minute)
print("Second:", current_date_time.second)

# Print formatted date and time
print("Year:", current_date_time.strftime("%Y"))
print("Month (full name):", current_date_time.strftime("%B"))
print("Day of the month:", current_date_time.strftime("%d"))
print("Hour:", current_date_time.strftime("%H"))
print("Minute:", current_date_time.strftime("%M"))
print("Second:", current_date_time.strftime("%S"))
print("Weekday (full name):", current_date_time.strftime("%A"))


"""What You’ve Learned:
You imported a module: The datetime module helps you work with date and time.
You retrieved and printed the current date and time: Using datetime.datetime.now(), you displayed both raw and formatted date and time.
You formatted output: strftime() allows you to format date and time in various ways.
By running this script, you’ve learned how to handle and format date and time in Python. 
Experiment with different format codes in strftime() to see how you can customize the output!"""