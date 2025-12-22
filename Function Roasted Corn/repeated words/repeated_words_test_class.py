from repeated_words import repeated_words

from unittest import TestCase

class TestClass (TestCase):

	def test_word_repetition_equality(self):

		validator = repeated_words("boy", 2)

		self.assertEqual(validator, "boyboy")

	def test_word_repetition_non_equality(self):

		validator = repeated_words("boy", 2)

		self.assertNotEqual(validator, "boy-boy")

	def test_word_repetition_with_wrong_argument(self):

		self.assertRaises(TypeError, lambda: repeated_words(2, "boy"))