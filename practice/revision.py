#How to define a function.
#You define a function.
#A function must have a doc string talking about what the functuion is about.
def greet_user(first_name , lastname='ilemobayo'):
    """Display a simple greeting."""
    print("Hello " + first_name.title() + " " + lastname.title() + "!")

greet_user(first_name='joseph')