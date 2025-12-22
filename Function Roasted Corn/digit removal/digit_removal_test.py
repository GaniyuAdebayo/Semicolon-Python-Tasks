from unittest import TestCase

from digit_removal import digit_removal

class TestClass (TestCase):

	def test_letters_left_are_not_equal (self):

		validator = digit_removal("amazing")

		self.assertNotEqual(validator, "aaig")

	def test_letters_left_are_equal (self):

		validator = digit_removal("semicolon")

		self.assertEqual(validator, "eioo")

	def test_when_number_is_passed (self):

		self.assertRaises(TypeError, lambda: digit_removal(654387))