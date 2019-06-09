#!/usr/bin/env python3

def main():
    animals = { 'kitten': 'meow', 'puppy': 'ruff!', 'lion': 'grrr',
        'giraffe': 'I am a giraffe!', 'dragon': 'rawr' }
    # animals = dict(kitten = 'meow', puppy = 'ruff!', lion = 'grrr', giraffe = 'I am a giraffe!', dragon = 'rawr')
    for k in animals.keys():
        print(k, end=' ', flush=True)
    print()
    for v in animals.values():
        print(v, end=' ',flush=True)
    print()
    print_dict(animals)
    # Insert a value into a dictionary
    animals['monkey'] = 'haha'
    print_dict(animals)
    # Search a key in a dictionary
    print('Yes!' if 'lion' in animals else 'No!')
    print(animals.get('chimpanzee'))

def print_dict(o):
    for x in o: print(f'{x}: {o[x]}')

if __name__ == '__main__':
	main()
