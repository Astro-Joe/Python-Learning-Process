import unittest
from city_function import city_country

class CityTestCase(unittest.TestCase):
    """test case for 'city_function.py'."""

    def test_city_country(self):
        """Do description like 'Ikorodu, Lagos' work?"""
        description = city_country('ikorodu', 'lagos')
        self.assertEqual(description, 'Ikorodu, Lagos')

unittest.main()