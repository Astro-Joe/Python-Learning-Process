# In this case the function is allowed to accept as much arguments as possible that is needed for the program to work.

# Like in making a pizza, you can't know before hand how many topping the customer wants
# Positional and arbitrary arguments can also be used together 

def make_pizza(size, *toppings): # The parameter 'toppings' is represented as a tuple
    """Print the toppings that have been requested"""
    
    print("\nMaking a " + str(size) +  "-inch pizza with the following toppings:")
    for topping in toppings:
        print('\t-' + topping.title())
    
make_pizza(18, 'pepperoni')
make_pizza(20, 'munshrooms', 'green peppers', 'extra cheese')