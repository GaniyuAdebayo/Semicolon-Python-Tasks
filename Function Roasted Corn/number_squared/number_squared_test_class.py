from unittest import TestCase

from number_squared import number_squared

class TestClass (TestCase):

	def test_equality_of_number_squared(self):

		validator = number_squared([2, 3, 4, 5, 7])

		self.assertEqual(validator, [4, 9, 16, 25, 49])

	def test_non_equality_of_number_squared(self):

		validator = number_squared([2, 3, 4, 5, 7])

		self.assertNotEqual(validator, [4, 6, 16, 25, 49])

	def test_eqality_with_negative_number(self):

		validator = number_squared([-2, 3, 4, -5, 7])

		self.assertEqual(validator, [4, 9, 16, 25, 49])

	def test_non_eqality_with_negative_number(self):

		validator = number_squared([-2, 3, 4, -5, 7])

		self.assertNotEqual(validator, [-4, 9, 16, -25, 49])

	def test_for_non_numeric(self):

		self.assertRaises(TypeError, lambda: number_squared([2, 3, 4, "few", 7]))