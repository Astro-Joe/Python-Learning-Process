git #alien_0 ={'color': 'green', 'points': 5}
#alien_1 ={'color': 'yellow', 'points': 10}
#alien_2 ={'color': 'red', 'points': 15}

aliens = []
#for alien in aliens:
  #  print(alien)

# make 30 aliens.
for alien_number in range(30): #range(30) specifies the amount of time the loop is going to run.
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
#for alien in aliens[:3]:
#    if alien['color'] == 'green':
 #       alien['color'] = 'yellow'
  #      alien['points'] = 10
   #     alien['speed'] = 'medium'
   # elif alien['color'] == 'yellow':
   #     alien['color'] = 'red'
   #     alien['speed'] = 'fast'
   #     alien['points'] = '15'
 
for alien in aliens[:5]:
  print(alien['color'])
print('...')

print('Total number of aliens: ' + str(len(aliens)))
