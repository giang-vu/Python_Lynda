#!/usr/bin/env python3

def main():
    f = open('lines.txt')   # "open" return a file object, so we can use a loop to read lines. Default mode is read-only
# open('lines.txt', 'w') to write, start from the begining
# open('lines.txt', 'a') to append
# open('lines.txt', 'r+w') to read and write
    for line in f:
        print(line.rstrip())    #rstrip() to strip the line ending of the file

if __name__ == '__main__':
	main()
