def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    # print(toppings) #python prints the output in a tuple
    # print(list(toppings)) # converts the tuple to a list
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("-", topping)


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
