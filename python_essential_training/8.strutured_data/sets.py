#!/usr/bin/env python3

# Set does not allow duplicates
def main():
    a = set("We're gonna need a bigger boat.")
    b = set("I'm sorry, Dave. I'm afraid I can't do that.")
    print_set(a)
    print_set(b)
    # If we want to print it in order, using sorted
    print_set(sorted(a))
    print_set(sorted(b))
    # Check the members in 2 sets
    print('Members in set a, but not in set b: ',end= '')
    print_set(sorted(a - b))
    
    print('Members in both set a and set b: ',end= '')
    print_set(sorted(a & b))
    
    print('Members in either set a or set b: ',end= '')
    print_set(sorted(a | b))
    
    print('Members in either set a or set b, but not both: ',end= '')
    print_set(sorted(a ^ b))
    
def print_set(o):
    print('{', end = '')
    for x in o: print(x, end = '')
    print('}')

if __name__ == '__main__':
	main()
