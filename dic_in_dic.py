users = {
    'aeinstein': {
        'first': input('Enter your fist name: '),
        'last': input("Enter you last name: "),
        'location': input('Enter your location: '),
        }, 
    'mcurie':{
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        }
}
for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + ' ' + user_info['last']
    location = user_info['location']

    print('\tFull name: ' + full_name.title())
    print('\tLocation:  ' + location.title())