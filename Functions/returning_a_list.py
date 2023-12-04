def greet_users(names):
    """Prints a simple greeting to each user in the list."""
    
    for name in names:
        message = 'Hello, ' + name.title() + '!'
        print(message)
        
usernames = ['joseph', 'tolulope', 'damilare', 'ifeoluwa']
greet_users(usernames)