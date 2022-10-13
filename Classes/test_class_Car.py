import unittest
from class_Car import *

class TestClassCar(unittest.TestCase):
    """Test cases for all classes and modules in class_Car.py"""

    def test_get_descriptive_name(self):
        """Test case for the method get_descriptive_name under class Car"""
        name = Car('honda', 'sport', 2016)
        result =  name.get_descriptive_name()
        self.assertEqual(result, '2016 Honda Sport')

unittest.main()