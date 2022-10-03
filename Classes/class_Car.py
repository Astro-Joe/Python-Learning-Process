class Car():
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0


    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")


    def update_odometer(self, mileage):
        """Set the odometer reading to a certain value"""
        self.odometer_reading = mileage
    

    def increment_odometer(self, mileage):
        """Add the given amount to the odometer reading"""
        self.odometer_reading += mileage

my_used_car = Car('audi', 'a4', 2016)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(50)
my_used_car.read_odometer()

my_used_car.increment_odometer(30)
my_used_car.read_odometer()


