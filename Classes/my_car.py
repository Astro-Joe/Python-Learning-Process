from class_Car import Car  # imports the class 'Car' from 'class_Car.py' module


my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
print(my_new_car.read_odometer())