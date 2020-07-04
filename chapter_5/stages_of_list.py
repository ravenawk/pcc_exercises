#!/usr/bin/env python3

persons_age = 5

if persons_age < 2:
    print("The person is a baby.")
elif persons_age >= 2 and persons_age < 4:
    print("The person is a toddler.")
elif persons_age >= 4 and persons_age < 13:
    print("The person is a kid.")
elif persons_age >= 13 and persons_age < 20:
    print("The person is a teenager.")
elif persons_age >= 20 and persons_age < 65:
    print("The person is an adult.")
elif persons_age > 65:
    print("The person is an elder.")
