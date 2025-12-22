
from unittest import TestCase

from continuous_noun import continuous_noun

class TestClass (TestCase):

	def test_for_ending_with_ing (self):

		valid_check = continuous_noun("drinking")

		self.assertEqual(valid_check, "drinkingly")

	def test_for_not_ending_with_ing (self):

		valid_check = continuous_noun("drink")

		self.assertEqual(valid_check, "drinking")

	def test_for_ending_with_ing_to_false(self):

		valid_check = continuous_noun("drinking")

		self.assertNotEqual(valid_check, "drinkinging")

	def test_for_ending_length_less_than_3(self):

		valid_check = continuous_noun("be")

		self.assertEqual(valid_check, "be")

	def test_for_word_with_number(self):

		self.assertRaises(TypeError, 5)	

	def test_for_word_with_number_within(self):

		self.assertRaises(TypeError, "ba3")	