import unittest
from class_Employee import Employee

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.employee = Employee("Joseph", "Ilemobayo")

    def test_give_default_raise(self):
        self.assertEqual = (self.employee.give_raise(), 5000)

    def test_give_custom_raise(self):
        self.employee.raiseAmount = 100
        self.assertEqual = (self.employee.give_raise(), 5100)


unittest.main()
