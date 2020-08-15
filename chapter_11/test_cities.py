#!/usr/bin/env python3

import unittest
from population import city_country_population

class CityCountryTestCase(unittest.TestCase):
    """Test for city_country from city_functions"""

    def test_city_coountry(self):
        """Test something like Santiago, Chile"""
        format_city = city_country_population('santiago', 'chile')
        self.assertEqual(format_city, 'Santiago, Chile')

    def test_city_coountry_population(self):
        """Test something like Santiago, Chile"""
        format_city = city_country_population('santiago', 'chile', 5000000)
        self.assertEqual(format_city, 'Santiago, Chile - 5000000')

if __name__ == '__main__':
    unittest.main()
