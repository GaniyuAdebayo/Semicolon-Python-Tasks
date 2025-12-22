from max_length import longest_word

from unittest import TestCase

class TestClass (TestCase):

	def test_for_longest_word(self):

		validator = longest_word(['welcome', 'out', 'weather', 'mobile', 'breakfast', 'journey'])

		self.assertEqual(validator, ("breakfast", 9))

	def test_for_not_longest_word(self):

		validator = longest_word(['welcome', 'out', 'weather', 'mobile', 'breakfast', 'journey'])

		self.assertNotEqual(validator, ("breakfast", 8))

	def test_for_value_not_string(self):

		self.assertRaises(TypeError, lambda: longest_word(['welcome', 2, 'weather', 'mobile', 'breakfast', 'journey']))