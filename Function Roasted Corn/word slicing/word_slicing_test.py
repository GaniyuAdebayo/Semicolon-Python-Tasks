from unittest import TestCase
from word_slicing import word_slicing

class TestClass (TestCase):

	def test_that_words_are_equal_for_length_greater_than_or_equal_to_4(self):

		is_valid = word_slicing("semicolon")
		self.assertEqual(is_valid, "seon")

	def test_that_words_are_not_equal_for_length_greater_than_or_equal_to_4(self):

		is_valid = word_slicing("semicolon")
		self.assertNotEqual(is_valid, "seno")

	def test_that_words_are_not_equal_for_length_greater_than_or_equal_to_3(self):

		is_valid = word_slicing("ate")
		self.assertNotEqual(is_valid, "aeea")

	def test_that_words_are_equal_for_length_greater_than_or_equal_to_3(self):

		is_valid = word_slicing("ate")
		self.assertEqual(is_valid, "aeae")

	def test_that_words_are_equal_for_length_less_than_or_equal_to_2(self):

		is_valid = word_slicing("on")
		self.assertEqual(is_valid, "onon")

	def test_that_words_are_not_equal_for_length_less_than_or_equal_to_2(self):

		is_valid = word_slicing("on")
		self.assertNotEqual(is_valid, "onno")

	def test_that_words_are_not_equal_for_length_less_than_or_equal_to_1(self):

		is_valid = word_slicing("I")
		self.assertNotEqual(is_valid, "ii")

	def test_that_words_are_equal_for_length_less_than_or_equal_to_1(self):

		is_valid = word_slicing("I")
		self.assertEqual(is_valid, "")

	def test_that_words_are_equal_for_length_equals_zero(self):

		is_valid = word_slicing("")
		self.assertEqual(is_valid, "")

	def test_that_words_are_equal_for_length_less_than_or_equal_to_1(self):

		is_valid = word_slicing("I")
		self.assertEqual(is_valid, "")

	def test_that_words_are_equal_for_words(self):

		is_valid = word_slicing("I am a boy")
		self.assertEqual(is_valid, "iaoy")

	def test_for_numbers(self):

		self.assertRaises(TypeError, lambda: word_slicing(456789))