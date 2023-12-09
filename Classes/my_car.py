from class_Car import *  # imports the class 'Car' from 'class_Car.py' module


# my_new_car = Car('audi', 'a4', 2016)
# print(my_new_car.get_descriptive_name())

# my_new_car.odometer_reading = -29
# print(my_new_car.read_odometer())

# my_new_car.update_odometer(30)
# print(my_new_car.read_odometer())
tesla = ElectricCar('tesla', 'f9', '2019')
tesla.battery.get_range()
tesla.battery.describe_battery()
tesla.battery.upgrade_battery()
tesla.battery.get_range()
tesla.battery.describe_battery()