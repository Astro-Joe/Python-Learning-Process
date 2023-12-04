# A function can be made to return complex data structures like lists and dictionaries
# Below is how a simple function that returns a dic. can be manipulated to get a desired result.

def build_car(name_of_car='', model_of_car=''):
    """Returns a dictionary containing the name and model of a car."""
    car = {'name':name_of_car, 'model' : model_of_car}
    return car



info = [] 

while True:
    print('\nEnter "q" to quit the process')
    car_name = input('Enter the name of the car: ')
    if car_name == 'q':
        break
    
    print('Enter "q" to quit')
    car_model = input('Enter the model of the car: ')
    if car_model == 'q':
        break
    
    
    sample_0 = build_car(car_name, car_model)
    info.append(sample_0)
print(info)
    
    

    