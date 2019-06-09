#
# Example file for working with timedelta objects
#

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

# Construct a basic timedelta and print it
print(timedelta(days = 365, hours = 5, minutes = 1))

# Print today's date
now = datetime.now()
print("Today's date is " + str(now))

# Print today's date one year from now
print("One year from now is " + str(now + timedelta(days = 365)))

# Create a timedelta that uses more than one argument
print("In 2 days and 3 weeks, it will be " + str(now + timedelta(days = 2, weeks = 3)))

# Calculate the date 1 week ago, formatted as a string
print("1 week ago was " + str(now + timedelta(weeks = -1)))
t = now - timedelta(days = 3)
print("3 days ago was " + t.strftime("%A, %B %d, %Y"))

# How many days until April Fools' Day?
today = date.today()
afd = date(today.year, 4, 1)

# Use date comparison to see if April Fool's has already gone for this year
# If it has, use the replace() function to get the date for next year
if afd > today:
    print("It's just " + str((afd - today).days) + " days until the April Fool's Day")
elif afd == today:
    print("The April Fool's Day is today")
else:
    print("The April Fool's has already gone " + str((today - afd).days) + " days ago")
    afd = afd.replace(year = today.year + 1)
    
    # Now calculate the amount of time until April Fool's Day
    print("It's just " + str((afd - today).days) + " days until the next April Fool's Day")
