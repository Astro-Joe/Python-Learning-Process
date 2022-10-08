from class_Car import ElectricCar, Car


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
#my_tesla.battery.describe_battery()
# my_tesla.fill_gas_tank()
# # my_tesla.battery.battery_size=85  # Changes the value of attribute battery_size
# # my_tesla.battery.describe_battery()
#my_tesla.battery.get_range()
# my_tesla.battery.upgrade_battery()

# my_tesla.battery.get_range()


my_car = Car('highlander', 'sports', '2020')
print('\n' + my_car.get_descriptive_name())
