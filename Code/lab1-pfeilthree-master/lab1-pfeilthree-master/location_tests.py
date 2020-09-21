# CPE 202 Location Class Test Cases, Lab 1

import unittest
from location import *

class TestLocation(unittest.TestCase):

    def test_repr(self):
        loc = Location('SLO', 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")
    def test_eq(self):
        loc1 = Location('place',101.1 , 162.2)
        loc2 = Location('place',101 , 162)
        self.assertNotEqual(loc1, loc2)
    def test_init(self):
        loc3 = Location('place', 50, 30)
        self.assertEqual(loc3.name, 'place')
        self.assertEqual(loc3.lat, 50)
        self.assertEqual(loc3.lon, 30)

if __name__ == "__main__":
        unittest.main()
