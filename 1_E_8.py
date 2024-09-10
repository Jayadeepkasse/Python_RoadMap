#Write a script that prints the current year.
import datetime
Now=datetime.datetime.now()
print(Now.strftime("%y"))
print(Now.year)
