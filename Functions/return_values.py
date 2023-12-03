# Basically,  return values allow the result of your function to be assigned to a variable and 
#be used in a flexible way in your code.
# Parameters can be made optional too. It uses the principle of default parameter value.

def get_formatted_name(first_name, last_name, middle_name= ''): # Here making the default value of middle_name an empty strings makes it an optional parameter
    """ Returns a full name, neatly formatted.
    Contains two parameters to get a full name and return the output of the function to the caller(assigned variable)."""
    
    full_name = first_name + ' ' + middle_name + ' ' + last_name
    return full_name.title()

sample_1 = get_formatted_name('joseph', 'ilemobayo')
print(sample_1)

sample_2 = get_formatted_name('joseph', 'ilemobayo', 'tolulope')
print(sample_2)