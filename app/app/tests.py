"""
Sample tests
"""
from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """ Test the calc module."""

    def test_add_numbers(self):
        """ Testing adding numbers together."""
        res = calc.add(5, 6)
        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        """ Test subtracting numbers together."""
        res = calc.subtract(4, 5)
        self.assertEqual(res, -1)
