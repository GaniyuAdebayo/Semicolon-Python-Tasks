
from unittest import TestCase

from string_length import string_length

class TestClass (TestCase):

	def test_check_length_of_word_equal(self):

		validator = string_length("semicolon")

		self.assertEqual(validator, 9)


	def test_check_length_of_word_not_equal(self):

		validator = string_length("semicolon")

		self.assertNotEqual(validator, 5)

	def test_check_length_of_integer_equal(self):

		validator = string_length(123456789)

		self.assertEqual(validator, 9)

	def test_check_length_of_integer_not_equal(self):

		validator = string_length(1234567890)

		self.assertNotEqual(validator, 9)