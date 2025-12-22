from unittest import TestCase

from min_number import min_number

class TestClass (TestCase):

	def test_for_min_number(self):

		validator = min_number([8, 4, 9, 2, 5, 7, 3])

		self.assertEqual(validator, 2)

	def test_for_not_min_number(self):

		validator = min_number([8, 4, 9, 2, 5, 7, 3])

		self.assertNotEqual(validator, 3)

	def test_for_min_number_with_negative_number(self):

		validator = min_number([8, 4, -9, 2, 5, 7, 3])

		self.assertEqual(validator, -9)

	def test_for_non_numeric(self):

		self.assertRaises(TypeError, lambda: min_number([8, 4, -9, "few", 5, 7, 3]))