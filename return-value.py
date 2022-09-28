def get_formatted_name(firstName, lastName):
    """Return a full name neatly formatted"""
    full_name = firstName + ' ' + lastName
    return full_name.title()


musician = get_formatted_name('joseph', 'ilemobayo')
print('my name is ' + musician)
