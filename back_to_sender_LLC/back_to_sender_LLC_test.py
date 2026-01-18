from unittest import TestCase

from back_to_sender_LLC import riderPay

class TestClass (TestCase):

	def test_for_sales_greater_than_70(self):

		validator = riderPay(75)
		self.assertEqual(validator, 42500)

	def test_for_sales_less_than_50(self):

		validator = riderPay(30)
		self.assertEqual(validator, 9800)

	def test_for_non_integer_value(self):

		validator = riderPay("number")
		self.assertEqual(validator, "Invalid input")

	def test_for_negative_integer_value(self):

		validator = riderPay(-5)
		self.assertEqual(validator, "Invalid input")

	def test_for_sales_greater_than_70_not_equal(self):

		validator = riderPay(75)
		self.assertNotEqual(validator, 4500)