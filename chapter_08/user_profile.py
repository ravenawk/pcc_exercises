#!/usr/bin/env python3
"""
Build out a user profile with unknow number of keyarguments
"""


def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info["first_name"] = first.title()
    user_info["last_name"] = last.title()
    return user_info


user_profile = build_profile(
    "steve", "rogers", location="new york", height="6 foot", sex="male"
)

for key, value in user_profile.items():
    print(key + " : " + value)
