#!/usr/bin/env python3

def main():
    game = [ 'Rock', 'Paper', 'Scissors', 'Lizard', 'Spock' ]
    # Searching in a list
    i = game.index('Paper')
    print(game[i])
    print_list(game)
    # Append an item
    game.append('Computer')
    print_list(game)
    # Insert an item to a position
    game.insert(0, 'Laptop')
    print_list(game)
    # Revome an item
    game.remove('Paper')
    print_list(game)
    # Remove the item with its index and return the removed one (without the index, remove the last item)
    x = game.pop(3)
    print(x)
    # Adding characters in every element
    print(',... '.join(game))

def print_list(o):
    for i in o: print(i, end=' ', flush=True)
    print()

if __name__ == '__main__':
	main()
