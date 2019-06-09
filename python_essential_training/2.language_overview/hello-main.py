#!/usr/bin/env python3

import platform

def main():
    message()

def message():
    print('This is python version {}'.format(platform.python_version()))
    print('Line 2')
    if True:    # This is a comment
        print('Line 3')
    else:
        print('Not True')

if __name__ == '__main__': main()
