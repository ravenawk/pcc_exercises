#!/usr/bin/env python3

import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Testing Employee class"""
    def test_give_default_raise(self):
        """Testing increase salary"""
        new_employee = Employee('Test', 'Employee', 50000)
        new_employee.increase_salary()
        self.assertEqual(new_employee.annual_salary, 55000)

    def test_give_custom_raise(self):
        """Testing increase salary"""
        new_employee = Employee('Test', 'Employee', 50000)
        new_employee.increase_salary(7500)
        self.assertEqual(new_employee.annual_salary, 57500)
        
unittest.main()

