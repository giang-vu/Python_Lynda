#!/usr/bin/env python3

def prime(n):
    if n < 0:
        return False
    elif n == 1:
        return True
    elif n == 2:
        return True
    for i in range(2,n):
        if n % i == 0:
            return False
    else:
            return True

x = 15
if prime(x):
    print(f'{x} is a prime')
else:
    print(f'{x} is not a prime')

def listPrimes():
    for i in range(100): # from 0 to 100, not including 100
        if prime(i):
            print(i, end = ' ', flush = True)

listPrimes()