responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name: ")
    response = input("Which mountain would you like to climb someday? ")

    responses[name] = response

    repeat = input("would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

print("\n------Poll Result------")
for name,response in responses.items():
    print(name + " would like to climb " + response + ".")