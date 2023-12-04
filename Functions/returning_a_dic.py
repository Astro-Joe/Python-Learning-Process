# A function can be made to return complex data structures like lists and dics

def build_car(name_of_car='', model_of_car=''):
    """Returns a list of info about inputed car"""
    
    info = []
    car = {'name':name_of_car, 'model' : model_of_car}
    info.append(car)
    
    print(info)
    return info

sample_0 = build_car('Highlander', '2023')
sample_1 = build_car('Rover', '2013')
