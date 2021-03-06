#!/usr/bin/env python3

def print_contents(filename):
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
            for line in lines:
                print(line.strip())
    except FileNotFoundError:
        pass

filenames = ['cats.txt', 'dogs.txt']
for somefile in filenames:
    print_contents(somefile)
