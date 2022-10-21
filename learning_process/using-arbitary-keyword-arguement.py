def build_profile(first, last, **user_info):  # The double asterisks before the parameter
    # **user_info cause Python to create
    # an empty dictionary called user_info and pack whatever name-value pairs it
    # receives into this dictionary.
    """Build a dictionary containing everything we know about a user."""
    profile = {'firstName': first.title(), 'last': last.title()}
    for key, value in user_info.items():
        profile[key] = value.title()
    return profile


user_profile = build_profile('joseph', 'ilemobayo', location='ikorodu', field='physics', hobby='star gazing')
print(user_profile)
