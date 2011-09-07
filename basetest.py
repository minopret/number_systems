from base import *
from math import sqrt, pi, e
import unittest

class TestBase(unittest.TestCase):
    # Enhancements that I'd like:
    # - do some tests of commutative operations
    # - use assertAlmostEqual or a similar custom construct
    #   to test that the representation has the requested
    #   accuracy

	def test1(self):
		result = to_non_integer_base(sqrt(2)**2, sqrt(2), -5)
		self.assertEqual(result, '100;0000')

	def test2(self):
		result = to_non_integer_base(2.0, sqrt(2.0), -15)
		self.assertEqual(result, '100;0000')

	def test3(self):
		result = to_non_integer_base(pi, e, -15)
		self.assertEqual(result, '10;10100202000211')

	def test4(self):
		result = to_non_integer_base(e, pi, -15)
		self.assertEqual(result,  '2;20212010021111')

if __name__ == '__main__':
    unittest.main()

