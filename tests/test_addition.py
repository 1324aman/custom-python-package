import unittest
from addition.addition import addition


class TestAddition(unittest.TestCase):

    def test_addition_of_two_numbers(self):
        self.assertEqual(addition(2, 2), 4)
