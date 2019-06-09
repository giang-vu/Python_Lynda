#!/usr/bin/env python3

# Default split is combine all spaces
s1 = 'This is a long string with a bunch of words in it.'
s2 = '''This
is              a long              string
with a bunch of words in it.'''
print(s1.split())
print(s2.split())

# Split by any character
print(s1.split('i'))

# Joining into a string
l = s1.split()
s3 = ':'.join(l)
print(s3)