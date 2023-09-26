import unittest
from divide.divide import divide


class TestDivision(unittest.TestCase):

    def test_division(self):
        self.assertEqual(divide(4, 2), 2.0)
