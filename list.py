friends = ['Debbie', 'joe', 'Sammie', 'Deborah']
print(friends)
#name_1 = friends[0]
#print(friends_1[0])
#print(friends[1].title())

#print(friends[0] + ' ' + friends[-1])
#message = 'My first friend was ' + friends[0]
#print(message)
#for i in friends:
#    print(i.title() + ' ' + 'is my friend')
friends[1] = 'Joseph'
friends[3] = 'Eniola'
print(friends)
friends.append('Darrell')
friends.append('Solace')
print(friends)
friends.insert(-1 , 'Omotola')
print(friends)
del friends[-1]
print(friends)
popped_friends = []
popped_friend_1 = friends.pop()
popped_friends.append(popped_friend_1)
print(popped_friend_1 + ' was removed from the list of friends.')
print(popped_friends)

friends.append(popped_friend_1)
print(popped_friend_1 + ' was added back!.')
print(friends)
popped_friend_2 = friends.pop(1)
popped_friends.append(popped_friend_2)
print(popped_friend_2 + ' was removed.')
print(popped_friends)
print(friends)
friends.remove('Omotola')
print(friends)