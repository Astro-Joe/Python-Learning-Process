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
        self.assertEqual(result, '\nThis car has 45 miles on it.' )
unittest.main()