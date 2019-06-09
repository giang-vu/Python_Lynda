#!/usr/bin/env python3

x = 42
y = 73

if x < y:
    z = 112
    print (f'x is smaller than y and x = {x} and y = {y}')
    print (f'{x} < {y}')
else:
    print (f'x is larger than y because x - y = {x-y}')

print (f'z is {z}') # block does not define the scope

# Python does not have switch case statement, we can use a chain of elifs instead
if x == 5:
    print ('Do 5 steps')
elif x == 7:
    print ('Do 7 steps')
elif x == 10:
    print ('Do 10 steps')
else:
    print ('Do many steps')