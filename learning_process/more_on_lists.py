
a_list = ['charles', 'martina', 'micheal', 'florence', 'eli']
#print(a_list[0:3])   #Slicing a list......
print('Here are the first three names in my list: ')
for name in a_list[:3]:
    print(name)
print('\n')
#second_list = a_list[:]
#print(second_list)

print('Three names from the middle in the list are: ')
for mid in a_list[1:4]:
    print(mid)
print('\n')

print('The last three names in the list are: ')
for last in a_list[-3:]:
    print(last)