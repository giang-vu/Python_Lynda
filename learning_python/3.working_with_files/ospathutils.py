#
# Example file for working with os.path module
#
import os
from os import path
import datetime
from datetime import date, time, timedelta
import time

def main():
    # Print the name of the OS
    print(os.name)

    # Check for item existence and type
    print("Item exists: " + str(path.exists("file1.txt")))
    print("Item is a file: " + str(path.isfile("file1.txt")))
    print("Item is a diretory: " + str(path.isdir("file1.txt")))
    
    # Work with file paths
    print("Item's path is: " + str(path.realpath("file1.txt")))
    print("Item's path and name: " + str(path.split(path.realpath("file1.txt"))))

    # Get the modification timedelta
    t = time.ctime(path.getmtime("file1.txt"))
    print(t)
    print(datetime.datetime.fromtimestamp(path.getmtime("file1.txt")))
    
    # Calculate how long ago the item was modified
    td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("file1.txt"))
    print("The file has been modified for {0} ago, or {1} seconds".format(td, td.total_seconds()))

if __name__ == "__main__":
    main()
