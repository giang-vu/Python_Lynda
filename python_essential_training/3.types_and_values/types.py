#!/usr/bin/env python3

x,y,z,t,w = 7,7.0,'4.5',True,None
print(type(x))  # "type" prints the type of variable. "If it walks like a duck, it is a duck"
print(type(y))
print(f'{type(z)} {type(t)} {type(w)}')

a = 'seven'
b = 'seven'.capitalize()
c = a.upper()

print(f'a is {a}, b is {b} and c is {c}')

d = 'seven {} {}'.format('eight', 9)
e = 'seven {1} {0}'.format('eight', 9)  # 1 and 0 will swap the position
f = f'seven {8:<8} {"nine":>09}'    # move the cursor left or right with leading characters

print(f'd is {d}, e is {e} and f is {f}')

g = 7/3
h = 7//3
print(f'g is {g} and type of g is {type(g)}')
print(f'h is {h}, type of h is {type(h)}')

# Problem of floating numbers so that it should not work with money
x = 0.1 * 3 - 0.3
print(f'x is {x} and type of x is {type(x)}')   # not equal to 0

# Fixing by importing decimal
from decimal import *   # import everything from decimal

a = Decimal('.1')
b = Decimal('.3')
x = a * 3 - b
print(f'x is {x} and type of x is {type(x)}')

y = 7 > 5
print(f'y is {y} and type of y is {type(y)}')

z = [1, 'two', 3.0]
t = (1, 'two', 3.0, [4, 'four'], 5)

print(f'z is {z} and type of z is {type(z)}')
print(f't is {t} and type of t is {type(t)}')
print(f'The 2nd element in t is {t[1]} and its type is {type(t[1])}')

# ID of an object
x = (1, 'two', 3.0, [4, 'four'], 5)
y = (1, 'two', 3.0, [4, 'four'], 5)
print(f'{id(x)} and {id(y)}')   # different values because of different objects
print(f'{id(x[0])} and {id(y[0])}')     # same values because of the same objects

if x[0] is y[0]:    # "is" is used to check whether same ID 
    print('Yes')
else:
    print('No')

if x is y:
    print('Yes')
else:
    print('No')

# Check type of x with "isinstance"
if isinstance(x, tuple):
    print('Yes')
else:
    print('No')