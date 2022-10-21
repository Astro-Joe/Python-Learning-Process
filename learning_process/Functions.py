# def greet_user(passwd, usr = 'astrojoe'): #the default value of usr is astrojoe
#     #There are parameteres in the brackets of the functon
#     """Display a simple greeting."""
#     print("\nHello, " + usr.title() + '!.')
#     print('Your password is ' + passwd)


# greet_user(passwd = '****', usr = 'debbie') #keyword argument


def make_shirt(text = 'I love Python', size = 'Large'):
    """Function to make a shirt"""
    print('The size of the shirt is ' + size)
    print('"' + text + '"'+ ' should be printed on the shirt.')


make_shirt(size = 'Medium')
