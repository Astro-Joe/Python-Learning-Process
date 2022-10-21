fav_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python' 
    }
print("Edward's favourite programming language is " + 
    fav_language['edward'].title() + 
    '\n'
    )

for name, language in fav_language.items(): #.item() method checks all the keys and values in the dictionary
    print(name.title() + "'s favourite language is " + 
    language.title() + '.\n')

friends = ['phil', 'sarah']
#for name in friends:
    #if name in fav_language.keys():
       # print(name.title() + ', thanks for taking this poll')
   # else:
       # print('Please ' + name.title() + ' take our poll')
for name in fav_language.keys():  # .key() method checks all the keys in the dictionary.
    print(name.title())
    if name in friends:
        print(" Hi " + name.title() + 
        ", I see your favourite language is " + 
        fav_language[name].title() + '!')
    if 'erin' not in fav_language.keys():
        print('Erin please take our poll.')
for name in sorted(fav_language.keys()): #sorted() function sorts all keys in the dic. in a =n orderly manner.
    print(name.title() + ', thank you for taking this poll!\n')

print('The following languages have been mentioned: ')
for languages in set(fav_language.values()): #The function set() is used to prevent repitition when printing out the result.
    print(languages.title()) 
print(fav_language.values())