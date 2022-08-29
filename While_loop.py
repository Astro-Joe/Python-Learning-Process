# currentNumber = 1
# while currentNumber <= 5:
#     print(currentNumber)
#     currentNumber += 1


#This program allows input and ends when the word quit is inpu
# prompt = '\nTell me something, and I will repeat it back to you:'
# prompt += '\n(Enter \'quit\' to end the program): '

# message = ""
# while message !='quit':
#     message = input(prompt)
#     if message != 'quit':
#         print(message)

# Using flags
# active = True
# while active:
#     message = input(prompt)
#     if message == 'quit':
#         active = False
#     else:
#         print(message)

# while True:
#     city = input(prompt)
#     if city  == 'quit':
#         break
#     else:

#         print("I'd love to go to " + city.title()+ '!')

currentNumber = 0
while currentNumber < 10:
    currentNumber += 1
    if currentNumber % 2 == 0:
        break
    print(currentNumber)