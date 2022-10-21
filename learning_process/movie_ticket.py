prompt = 'Enter your age'
prompt += '\n(Type stop to stop the program): '
# active =True
# while active:
#     reply = input(prompt)
#     if reply == 'stop':
#         active = False
#     elif int(reply) < 3:
#         print('The ticket is free.')
#     elif int(reply) in range(3,13):
#         print('The ticket is $10')
#     elif int(reply) > 12:
#         print('The ticket is $15')
    
# age  = ''
# while age != 'stop':
#     age = input(prompt)
#     if age == 'stop':
#         print('program ended')
    
#     elif int(age) < 3:
#         print('The ticket is free.')
#     elif int(age) in range(3,13):
#         print('The ticket is $10')
#     elif int(age) > 12:
#         print('The ticket is $15')


age  = ''
while age != 'stop':
    age = input(prompt)
    if age == 'stop':
        break
    elif int(age) < 3:
        print('The ticket is free.')
    elif int(age) in range(3,13):
        print('The ticket is $10')
    elif int(age) > 12:
        print('The ticket is $15')

    
    
    
        

    