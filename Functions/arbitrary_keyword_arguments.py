# This can be used whenyou plan to accept many key-value pairs as the calling statement provides.
#This works real good when working with dictionaries.

# Arbitrary parameter is used to accept a key-value item.
def build_profile(first, last, **usr_info): # The data structure of a parameter with a double asterik is a dictionary.
    """Build a dictionary containing everything we know about a user."""
    
    profile = {}
    profile['first_name'] = first.title()
    profile['last_name'] = last.title()
    for key,value in usr_info.items():
        profile[key] = value.title()
    return profile

usr_profile = build_profile('joseph', 'ilemobayo',
                            location = 'lagos',
                            field = 'physics',
                            age = '17')

print(usr_profile)