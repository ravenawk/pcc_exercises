#!/usr/bin/env python3
'''
Pick the right age name
'''

PERSONS_AGE = 5

if PERSONS_AGE < 2:
    print("The person is a baby.")
elif 4 < PERSONS_AGE >= 2:
    print("The person is a toddler.")
elif 13 > PERSONS_AGE >= 4:
    print("The person is a kid.")
elif 20 > PERSONS_AGE >= 13:
    print("The person is a teenager.")
elif 65 > PERSONS_AGE >= 20:
    print("The person is an adult.")
elif PERSONS_AGE > 65:
    print("The person is an elder.")
