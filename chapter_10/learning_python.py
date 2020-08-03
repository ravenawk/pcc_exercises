#!/usr/bin/env python3

with open('can_do_in_python.txt') as fileobject:
    lines = fileobject.read()
    print(lines)
print("")

with open('can_do_in_python.txt') as fileobject:
    for line in fileobject:
        print(line.strip())
print("")

with open('can_do_in_python.txt') as fileobject:
    lines = fileobject.readlines()

for line in lines:
    print(line.strip())

