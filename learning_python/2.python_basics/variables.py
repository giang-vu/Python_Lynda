#
# Example file for variables
#

# Declare a variable and initialize it
foo = 123
print(foo)

# Re-declaring the variable works
foo = "abc"
print(foo)

# ERROR: variables of different types cannot be combined
print("This is a string " + str(123))

# Global vs. local variables in functions
def someFunction():
    global foo
    foo = "def"
    print(foo)

someFunction()
print(foo)
