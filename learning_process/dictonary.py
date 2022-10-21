alien_0 = {'color': 'green', 'points': 5}
print(str(alien_0) + '\n')

alien_0['x_position'] = 0 #adding new key-value to existing dictionary.
alien_0['y_position'] = 25
print(str(alien_0) + '\n')


alien_0['color'] = 'yellow'
print(str(alien_0) + '\n')

alien_0['speed'] = 'medium'
#alien_0['speed'] = 'fast'
print(str(alien_0) + '\n')
print('Original x-position: ' + str(alien_0['x_position']))

#move the alien to the right and determine how far the alien should move based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
alien_0['x_position'] = alien_0['x_position'] + x_increment
print('\nNew x-position: ' + str(alien_0['x_position']))
del alien_0['points']

print(alien_0)