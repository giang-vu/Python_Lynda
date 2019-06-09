#
# Read and write files using the built-in Python file methods
#

def main():
    # Open a file for writing and create it if it doesn't exist
    f1 = open("file1.txt", "w+")
    
    # Open the file for appending text to the end
    f2 = open("file2.txt", "a+")
    for i in range (1,10):
       f2.write("This is line {0} \r\n".format(i))
    f2.close()

    # Write some lines of data to the file
    for i in range (1,10):
        f1.write("This is line {0} \r\n".format(i))
        
    # Close the file when done
    f1.close()
    
    # Open the file back up and read the contents
    # READ THE WHOLE FILE
    f1 = open("file1.txt", "r")

    if f1.mode == 'r':
        contents = f1.read()
        print(contents)
    else:
        print("There exists an error when open the file")
    
    # READ BY LINES
    f1 = open("file1.txt", "r")

    if f1.mode == 'r':
        lines = f1.readlines()
        for i in lines:
            print(i)
    else:
        print("There exists an error when open the file")

if __name__ == "__main__":
    main()
