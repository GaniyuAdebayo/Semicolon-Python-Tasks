from unittest import TestCase

from number_squared_sum import number_squared_sum

class TestClass (TestCase):

	def test_the_equality_of_sum_square(self):

		validator = number_squared_sum([2, 3, 4, 5, 7])

		self.assertEqual(validator, 103)

	def test_the_non_equality_of_sum_square(self):

		validator = number_squared_sum([2, 3, 4, 5, 7])

		self.assertNotEqual(validator, 100)

	def test_for_non_numeric(self):

		self.assertRaises(TypeError, lambda: number_squared_sum([2, 3, 4, "few", 7]))