import unittest
from class_Car import *

class TestClassCar(unittest.TestCase):
    """Test cases for all classes and modules in class_Car.py"""

    def test_get_descriptive_name(self):
        """Test case for the method get_descriptive_name under class Car"""
        name = Car('honda', 'sport', 2016)
        result =  name.get_descriptive_name()
        self.assertEqual(result, '2016 Honda Sport')

    def test_read_odometer(self):
        """Test case for the method read_odometer under class Car"""
        name = Car('benz', 'luxury', 2022)
        name.odometer_reading = 32
        result = name.read_odometer()
        self.assertEqual(result, '\nThis car has 32 miles on it.')

    def test_update_odometer(self):
        """Test case for the method update_odometer under class Car"""
        name = Car('benz', 'luxury', 2022)
        name.update_odometer(45)
        result = name.read_odometer()
        self.assertEqual(result, '\nThis car has 45 miles on it.')

    def test_increment_odometer(self):
        """Test case for the method update_odometer under class Car"""
        name = Car('benz', 'luxury', 2022)
        name.increment_odometer(20)
        result = name.read_odometer()
        self.assertEqual(result, '\nThis car has 20 miles on it.')

    def test_fill_gas_tank(self):
       """Test case for the method fill_gas_tank under class Car""" 
       name = Car('benz', 'luxury', 2022)
       name.gas_tank = 15
       result = name.fill_gas_tank()
       self.assertEqual(result, "\nYour gas tank is 15 litres.")

    def test_update_odometer_2(self):
        """Test case to show  that the odometer can't be rolled back"""
        name = Car('benz', 'luxury', 2022)
        name.odometer_reading = 21
        result = name.update_odometer(20)
        self.assertEqual = (result, "\nYou can't roll back an odometer")


unittest.main()