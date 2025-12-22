from credit_card import *

from unittest import TestCase

class TestClass (TestCase):

	def test_for_card_number_with_letter(self):

		self.assertRaises(RuntimeError, lambda: credit_card_number("438757601e402626"))

	def test_for_card_number_with_number_only_of_length_between_13_and_16(self):

		validator = credit_card_number("4387576017402626")

		self.assertEqual(validator, "4387576017402626")


	def test_for_card_number_with_hyphen_and_space(self):

		validator = credit_card_number("4387 5760 1740-2626")

		self.assertEqual(validator, "4387576017402626")	


	def test_for_card_number_with_number_only_of_length_below_13(self):

		self.assertRaises(RuntimeError, lambda: credit_card_number("438757601740"))


	def test_for_card_number_with_number_only_of_length_above_16(self):

		self.assertRaises(RuntimeError, lambda: credit_card_number("438757601740262626"))

	
	def test_for_credit_card_type_with_correct_number_for_visa(self):

		validator = credit_card_type("4387 5760 1740-2626")

		self.assertEqual(validator, "Visa Card")

	def test_for_credit_card_type_with_correct_number_for_master_card(self):

		validator = credit_card_type("5387 5760 1740-2626")

		self.assertEqual(validator, "Master Card")

	def test_for_credit_card_type_with_correct_number_for_Discover_card(self):

		validator = credit_card_type("6387 5760 1740-2626")

		self.assertEqual(validator, "Discover Card")

	def test_for_credit_card_type_with_correct_number_for_American_Express(self):

		validator = credit_card_type("3787 5760 1740-2626")

		self.assertEqual(validator, "American Express Card")

	def test_for_credit_card_type_with_correct_number_for_invalid_card(self):

		validator = credit_card_type("7787 5760 1740-2626")

		self.assertEqual(validator, "Invalid Card")

	def test_for_credit_card_type_with_incorrect_number(self):

		self.assertRaises(RuntimeError, lambda: credit_card_type("387 560 140-266"))

	def test_for_validity_status_with_invalid_number(self):

		validator = credit_card_validity_status("4387 5760 1740-2626")

		self.assertEqual(validator, "Invalid")

	def test_for_validity_status_with_valid_number(self):

		validator = credit_card_validity_status("5399-8316 1969-0403")

		self.assertEqual(validator, "Valid")

		
	def test_for_validity_status_with_incorrect_number(self):


		self.assertRaises(RuntimeError, lambda: credit_card_validity_status("387 560 140-266"))
	