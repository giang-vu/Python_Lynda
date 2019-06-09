#!/usr/bin/env python3


import sys
import os

def main():
    v = sys.version_info
    print('Python version {}.{}.{}'.format(*v))
    print(sys.platform)
    print(os.name)
    print(os.getenv('PATH'))
    print(os.getcwd())
    print(os.urandom(25).hex()) # 25 bytes long

if __name__ == '__main__': main()
