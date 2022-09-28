# def greet_user(names):
#     """Prints a simple greeting to each user in a list"""
#     for name in names:
#         msg = "Hello, " + name.title() + "!"
#         print(msg)


# userNames = ['joseph', 'tolulope', 'damilare', 'ifeoluwa']
# greet_user(userNames)



def print_models(unprintedDesign, completedDesign):
    while unprintedDesign:
        currentDesign = unprintedDesign.pop()
        print('Printing ' + currentDesign)
        completedDesign.append(currentDesign)

def display_models(completedDesign):
    print("\nThe following designs have been printed: ")
    for design in completedDesign:
        print(design)


designs = ['iphone case', 'robot pendant', 'dodecahedron']
finishedDesign = []

print_models(designs[:], finishedDesign) # The first argument passes a copy of the original list.
display_models(finishedDesign)

# sth = designs
# print(sth)