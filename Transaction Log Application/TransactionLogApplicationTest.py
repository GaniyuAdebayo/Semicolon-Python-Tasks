from unittest import TestCase
from TransactionLogApplication import *

class TestClass (TestCase):

	def test_for_deposit(self):

		transactions = []
		validator = deposit(4311, 0.0, transactions)

		self.assertEqual(validator, 4311.00)

	def test_for_withdrawal(self):

		transactions = []
		validator = withdraw(4300, 5000, transactions)

		self.assertEqual(validator, 700.00)

	def test_for_deposit_not_equal(self):

		transactions = []
		validator = deposit(4311, 0.0, transactions)

		self.assertNotEqual(validator, 4300.00)

	def test_for_withdrawal_not_equal(self):

		transactions = []
		validator = withdraw(4300, 5000, transactions)

		self.assertNotEqual(validator, 600.00)

	def test_for_withdrawal_more_than_balance(self):

		transactions = []
		validator = withdraw(4300, 4000, transactions)

		self.assertNotEqual(validator, 600.00)