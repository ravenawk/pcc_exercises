#!/usr/bin/env python3

users = {
        'aeinstein': {
            'first': 'albert',
            'last': 'einstein',
            'location': 'princeton'
            },
        'mcuri': {
            'first': 'marie',
            'last': 'curie',
            'location': 'paris'
            }
        }

for username, userinfo in users.items():
    full_name = f"{userinfo['first'].title()} {userinfo['last'].title()}"
    print(f"{full_name} is located in {userinfo['location'].title()}.")
