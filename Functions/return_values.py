# Basically,  return values allow the result of your function to be assigned to a variable and 
#be used in a flexible way in your code.

def get_formatted_name(first_name, last_name):
    """ Returns a full name, neatly formatted.
    Contains two parameters to get a full name and return the output of the function."""
    
    full_name = first_name + ' ' + last_name
    return full_name.title()

sample_1 = get_formatted_name('joseph', 'ilemobayo')
print(sample_1)
    
    