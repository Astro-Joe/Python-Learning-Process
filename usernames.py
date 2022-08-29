current_users = ['Joseph', 'John','Samuel', 'Tayo', 'Dayo'] 
new_users = ['JOSEPH', 'Haridun', 'samuel']

for user in current_users:
    if user.upper() or user.title() in new_users:
        print('This username is unavailable.\nEnter a new username.\n')
    else:
        print('Username available.\n')