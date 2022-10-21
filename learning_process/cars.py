def make_car(manufacturer, model, **others):
    car = {'manufacturer': manufacturer.title(), 'model': model.title()}
    for key, value in others.items():
        car[key] = value
    return car
