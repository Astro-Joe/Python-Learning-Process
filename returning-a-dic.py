def build_person(firstName, lastName, age = ''):
    """Return a dictionary of information about a person."""
    person = {'first': firstName, 'last': lastName}
    if age:
        person['age'] = age
    return person


musician = build_person('joseph', 'ilemobayo', age = 16)
print(musician)
# for key,value in musician.items(): #confirmation that its a dictionary
#     print(key + ': ' + value)