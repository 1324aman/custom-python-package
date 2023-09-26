import unittest
from subtract.subtract import subtract


class TestSubtraction(unittest.TestCase):

    def test_subtraction(self):
        self.assertEqual(subtract(4, 2), 2)
