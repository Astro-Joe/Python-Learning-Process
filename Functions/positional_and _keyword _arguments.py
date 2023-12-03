# Using positional arguments the arguremnts have to be in the same order as the parameter
def name_of_pet(animal_type, pet_name):
    """Prints out the name and type of pet."""
    
    print('The name of my ' + animal_type.title() + ' is ' + pet_name)
    
name_of_pet()