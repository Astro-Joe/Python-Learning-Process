# In this case the function is allowed to accept as much arguments as possible that is needed for the program to work.

# Like in making a pizza, you can't know before hand how many topping the customer wants

def make_pizza(*toppings): # The parameter 'toppings' is represented as a tuple
    """Print the toppings that have been requested"""
    
    print("\nMaking pizza with the following toppings:")
    for topping in toppings:
        print('\t-' + topping.title())
    
make_pizza('pepperoni')
make_pizza('munshrooms', 'green peppers', 'extra cheese')