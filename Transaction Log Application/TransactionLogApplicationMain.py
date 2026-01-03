from TransactionLogApplication import *

transactions = []
account_balance = 0.0

while (True):
	log_app = """

	Welcome to Transaction Log App

	1. Deposit
	2. Withdrawal
	3. Show Transactions
	4. Exit

	"""

	print(log_app)

	main_menu = int(input("Enter your choice: "))

	match (main_menu):

		case 1:

			amount = float(input("Enter deposit amount: "))
			account_balance = deposit(amount, account_balance, transactions)

		case 2:

			amount = float(input("Enter withdrawal amount: "))
			account_balance = withdraw(amount, account_balance, transactions)

		case 3:

			show_transaction(transactions)

		case 4:

			print(f"Final Balance: N{account_balance}")
			print("Thank you for using Transaction Log App")
			break

		case _:
			print ("Invalid number")

