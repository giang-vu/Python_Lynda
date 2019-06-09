#
# Example file for working with loops
#

def main():
    x = 0
    
    # Define a while loop
    while (x < 5):
        print(x)
        x = x + 1
    
    # Define a for loop
    for i in range(5, 10, 2):
        print(i)
        
    # Use a for loop over a collection
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    for d in days:
        print(d)
        
    # Use the break and continue statements
    for i in range(1, 10):
        if (i == 7):
            break
        if (i % 2 == 0):
            continue
        print(i)
        
    # Using the enumerate() function to get index
    for i, d in  enumerate(days):
        print(str(i) + " is index of " + str(d))

if __name__ == "__main__":
    main()
