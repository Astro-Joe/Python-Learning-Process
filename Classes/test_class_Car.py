import unittest
from class_Car import *

class TestClassCar(unittest.TestCase):
    """Test cases for all classes and modules in class_Car.py"""

    def setUp(self):
        self.name = Car('honda', 'sport', 2016)

    def test_get_descriptive_name(self):
        """Test case for the method get_descriptive_name under class Car"""
        result =  self.name.get_descriptive_name()
        self.assertEqual(result, '2016 Honda Sport')

    def test_read_odometer(self):
        """Test case for the method read_odometer under class Car"""
        self.name.odometer_reading = 32
        self.assertEqual(self.name.read_odometer(), '\nThis car has 32 miles on it.')

    def test_update_odometer(self):
        """Test case for the method update_odometer under class Car"""
        self.name.update_odometer(45)
        self.assertEqual(self.name.read_odometer(), '\nThis car has 45 miles on it.')

    def test_increment_odometer(self):
        """Test case for the method update_odometer under class Car"""
        self.name.increment_odometer(20)
        self.assertEqual('\nThis car has 20 miles on it.', self.name.read_odometer())

    def test_fill_gas_tank(self):
       """Test case for the method fill_gas_tank under class Car""" 
       self.name.gas_tank = 15
       self.assertEqual(self.name.fill_gas_tank(), "\nYour gas tank is 15 litres.")

    def test_update_odometer_2(self):
        """Test case to show  that the odometer can't be rolled back"""
        self.name.odometer_reading = 21
        self.assertEqual = (self.name.update_odometer(20), "\nYou can't roll back an odometer")


unittest.main()