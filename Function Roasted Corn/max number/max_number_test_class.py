from unittest import TestCase

from max_number import max_number

class TestClass (TestCase):

	def test_for_max_number(self):

		validator = max_number([8, 4, 9, 2, 5, 7, 3])

		self.assertEqual(validator, 9)

	def test_for_not_max_number(self):

		validator = max_number([8, 4, 9, 2, 5, 7, 3])

		self.assertNotEqual(validator, 3)

	def test_for_max_number_with_negative_number(self):

		validator = max_number([8, 4, -9, 2, 5, 7, 3])

		self.assertEqual(validator, 8)

	def test_passing_of_non_numeric (self):

		self.assertRaises(TypeError, lambda: max_number([8, 4, -9, "few", 5, 7, 3]))