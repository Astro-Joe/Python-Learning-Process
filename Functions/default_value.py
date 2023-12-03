# Sometimes the argument of a certain parameter of a function can be set to a default value.
def pet_name(pet_name, animal_type='dog'): # The parameter with the default valuye always comes second.
    """Prints out name of a pet"""
    
    print('The name of my ' + animal_type + ' is ' + pet_name.title())
    
    
pet_name('wille') # Uses the default value for animal_type
pet_name('wille', 'cat') # Uses 'cat' as the value of animal_type.
