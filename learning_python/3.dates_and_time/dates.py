#
# Example file for working with date information
#

from datetime import date
from datetime import time
from datetime import datetime

def main():
    ## DATE OBJECTS
    # Get today's date from the simple today() method from the date class
    today = date.today()
    print("Today's date is " + str(today))
    
    # Print out the date's individual components
    print("Date's components: " + str(today.day) + ", " + str(today.month) + " and " + str(today.year))
    
    # Retrieve today's weekday (0=Monday, 6=Sunday)
    print("Today's weekday number is " + str(today.weekday()))
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    print("which is a " + days[today.weekday()])
    
    ## DATETIME OBJECTS
    # Get today's date from the datetime class
    today = datetime.now()
    print("The current date and time is " + str(today))

    # Get the current time
    time = datetime.time(today)
    print(time)

if __name__ == "__main__":
    main()
  
