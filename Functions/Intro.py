def greet_user(username):  # The keyword "def" is used to inform python that you are defining a function. This function requires a parameter
    """Displays a simple greeting""" # A docstring used to describe what the functon does.
    
    print("Hello " + username.title() + '!.') # The task the function is designed to carry out.
    
greet_user('joSePh') # Calling the function. An argument was passed when calling this function.

