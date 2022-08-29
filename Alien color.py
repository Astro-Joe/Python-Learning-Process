user = input('Type a color: ')
user = user.lower()
alien_color = ['green', 'yellow', 'red']
if user in alien_color and user == 'green':
    print('\nYou earned 5 points.')
elif user in alien_color and user == 'red':
    print('\nYou earned 15 points.')
elif user in alien_color and user == 'yellow':
    print('\nYou earned 10 points.')
