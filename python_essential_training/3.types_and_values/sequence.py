#!/usr/bin/env python3

x = [ 1, 2, 3, 4, 5 ]
for i in x:
    print('i is {}'.format(i))

for i in range(5):
    print(i, end = ' ', flush = True)
print()     # enter

for i in range(1,5):
    print(i, end = ' ', flush = True)
print()

for i in range(1,50,5):     # increment by 5
    print(i, end = ' ', flush = True)
print()

# Assign the number in the sequence
x = list(range(5))
x[2] = 100
for i in x:
    print(f'i is {i}')

# A dictionary (key : value) or dict(key = value)
x = {'one':1, 2:'two', 'three':3, 4:'four', 'five':5.0}
for i in x:
    print(f'i is {i}') # print only keys

# A dictionary is mutable, so we can assign a new value to a key
x['three'] = 'THREE'
for k, v in x.items():
    print(f'key: {k} and value: {v}')   # print both keys and values

