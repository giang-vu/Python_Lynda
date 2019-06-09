#
# Example file for working with Calendars
#

# Import the calendar module
import calendar

# Create a plain text calendar
# Set Sunday as the begining of the week
c = calendar.TextCalendar(calendar.SUNDAY)
st = c.formatmonth(2017, 1, 0, 0)
print(st)

# Create an HTML formatted calendar
hc = calendar.HTMLCalendar(calendar.MONDAY)
st = hc.formatmonth(2018, 2)
print(st)

# Loop over the days of a month
# Zeroes mean that the day of the week is in an overlapping month

  
# The Calendar module provides useful utilities for the given locale,
# such as the names of days and months in both full and abbreviated forms


# Calculate days based on a rule: For example, consider
# a team meeting on the first Friday of every month.
# To figure out what days that would be for each month,
# we can use this script:
  
