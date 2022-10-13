import unittest 
from return_value import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Test case for 'return_value.py'."""

    def test_first_last_name(self):
        """Do names like 'Joseph Ilemobayo' work?"""
        formatted_name = get_formatted_name('joseph', 'ilemobayo')
        self.assertEqual(formatted_name, 'Joseph Ilemobayo')

    def test_first_last_middle_name(self):
        """Do names like 'Joseph Tolulope Ilemobayo' work?"""
        formatted_name = get_formatted_name('joseph', 'ilemobayo', 'tolulope')
        self.assertEqual(formatted_name, 'Joseph Tolulope Ilemobayo')


unittest.main() 