prompt = "Which toppings do you want on you pizza!"
prompt += "\n(Enter when you done listing:) "

message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print('Adding ' + message.title()+ '...')
    else:
        print('Your pizza is ready!')

     