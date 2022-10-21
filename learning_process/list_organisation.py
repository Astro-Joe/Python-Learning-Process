things = ['game pad', 'laptop', 'data', 'food']
print(things)
#things.sort() #arranges list permanently in an alphabetic order.
#print(things)

#print('\n')
#things.sort(reverse=True) #arranges list permanently in a reverse alphabetic order.
#print(things)

print('\n')
print(sorted(things)) #Temporarily arranges list in an alphabetic order
print(things)
#new = sorted((things)reverse=True)
#print(new)
things.reverse()
print(things)
print(len(things))