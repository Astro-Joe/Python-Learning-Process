def display_message(): # Without passing a parameter
    """Displays message to a particular group of people."""
    
    people = ['ayo', 'tolu', 'dami', 'joseph']
    for name in people:
        print(name.title() + ' I am learning how to write functions in this chapter.')
        
display_message()


def favourite_book(title):
    """Prints a sentence about a favourite book"""
    
    print(title.title() + ' is one of my favourite book.')
    
favourite_book('hyperspace')