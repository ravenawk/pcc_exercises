#!/usr/bin/env python3

class Employee():
    """Represent an Employee"""
    def __init__(self, first_name, last_name, annual_salary):
        """Initialize Employee object"""
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def increase_salary(self, increase=5000):
        """Increase annual_salary"""
        self.annual_salary += increase
        print(self.annual_salary)

frank = Employee('Frank', 'Chance', 50000)
frank.increase_salary()