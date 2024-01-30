"""
sample tests
"""
from django.test import SimpleTestCase
from app import calc


class CalcTests(SimpleTestCase):
    """
    test calc module
    """
    def test_add_numbers(self):
        """
        test add numbers
        """
        self.assertEqual(calc.add(3, 8), 11)

    def test_subtract_numbers(self):
        """
        test subtract numbers
        """
        self.assertEqual(calc.subtract(5, 11), 6)
