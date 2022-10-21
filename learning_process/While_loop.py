# Basic exampleof while loop
# currentNumber = 1
# while currentNumber < 5:
#     print(currentNumber)
#     currentNumber += 1

# Using a value to quit a while loop
# message = ''
# while message != 'quit':
#     message = input("\nTell me something and I'll repeat it back to you: \nEnter 'quit' to end the program ")
#     if message != 'quit':
#         print(message)

# Using a flag
#A flag is used when there are a lot of conditions that can make the while loop stop.
# promp = '\nTell me anything and I will give you back'
# promp += '\nEnter \'quit\' to end the program: '
# message = ''

# active = True
# while active:
#     message = input(promp)
#     if message == 'quit':
#         active =False
        
        
#Using break
#This is used to end the loop immediately a condition has been met
while True:
    city = input('\nEnter a name of a city. \nEnter "quit" when you are done')
    if city ==  'quit':
        break
    else:
        print('You have visited ' + city.title())