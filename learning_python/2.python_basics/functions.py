#
# Example file for working with functions
#

# Define a basic function
def function1():
    print("I am a function")

function1()
print(function1())

# Function that takes arguments
def function2(arg1, arg2):
    print(arg1, " and ", arg2)

function2(10, 20)
print(function2(10, 20))

# Function that returns a value
def cube(x):
    return x*x*x

print(cube(5))

# Function with default value for an argument
def power(num, x = 1):
    result = 1
    for i in range(x):
        result = result * num
    return result

print(power(2))
print(power(2,4))
print(power(x = 4, num = 2))

# Function with variable number of arguments
def multiAdd(*x):
    result = 0
    for i in x:
        result = result + i
    return result

print(multiAdd(10, 20, 30, 40))



