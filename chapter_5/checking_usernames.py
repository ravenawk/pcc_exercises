#!/usr/bin/env python3
'''
Comparing users
'''

lower_current_users = []

current_users = ['peter', 'steve', 'tony', 'bruce', 'miles']
for user in current_users:
    lower_current_users.append(user)

new_users = ['clark', 'bruce', 'ric', 'dianna', 'billy']

for new_user in new_users:
    if new_user.lower() in lower_current_users:
        print(f"{new_user} is not available, please choose another.")
    else:
        print(f"The username {new_user} is available.")
