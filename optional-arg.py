def get_formatted_name(firstName, lastName, middleName = ''):
    """Return a full name neatly formatted"""
    if middleName:
        full_name = firstName + ' ' + middleName + ' ' + lastName
    else:
        full_name = firstName + ' ' + lastName
    return full_name.title()


musician = get_formatted_name('joseph', 'ilemobayo')
print(musician)

musician =get_formatted_name('joseph', 'ilemobayo', 'tolulope')
print(musician)