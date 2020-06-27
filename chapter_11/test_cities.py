import unittest
from city_functions import city_function

class TestingCities(unittest.TestCase):

    def test_city_country(self):
        city_and_country = city_function('santiago', 'chile')
        self.assertEqual(city_and_country, 'Santiago, Chile - population ')

    def test_city_country_population(self):
        city_and_country = city_function('santiago', 'chile', 5000000)
        self.assertEqual(city_and_country, 'Santiago, Chile - population 5000000')

if __name__ == "__main__":
    unittest.main()