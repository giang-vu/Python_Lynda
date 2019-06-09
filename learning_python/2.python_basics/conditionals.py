#
# Example file for working with conditional statements
#

def main():
    x, y = 10, 100
    
    # Conditional flow uses if, elif, else
    if x < y:
        string = "x is smaller than y"
    elif x == y:
        string = "x is equal to y"
    else:
        string = "x is greater than y"

    print(string)
    
    # Conditional statements let you use "a if C else b"
    st = "x is smaller than y" if (x < y) else "x is greater than or equal to y"

    print(st)

if __name__ == "__main__":
    main()
