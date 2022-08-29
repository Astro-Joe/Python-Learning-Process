users = ['Joseph', 'Tolu', 'Admin', 'Dayo']
for user in users:
    if 'Admin' in user:
        print('Hello Admin, would you like to see a status report?')
    else:
        print('Hello ' + user + ', thank you for logging in again.')