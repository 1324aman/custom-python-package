import unittest
from multiply.multiply import multiply


class TestMultiplication(unittest.TestCase):

    def test_multiplication(self):
        self.assertEqual(multiply(2, 2), 4)
