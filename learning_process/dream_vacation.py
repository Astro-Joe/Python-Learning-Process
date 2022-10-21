poll = True
Vacay = {}

while poll:
    name = input("\nWhat is your name? ")
    place = input("Where would you like to visit for vacation? ")
    Vacay[name] = place
    option = input("Would you want another person to respond? (yes/no) ")
    if option == 'no':
        poll = False
    else:
        continue
print(Vacay)

print("====Poll Result====")
for key, value in Vacay.items():
    print(key.title() + " would want to go to " + value.title())
