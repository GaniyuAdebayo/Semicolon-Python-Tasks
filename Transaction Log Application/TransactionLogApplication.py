
def deposit(amount, account_balance, transactions):

	account_balance += amount
	
	transaction = f"Deposited: N{amount} | New Balance: N{account_balance}"

	print(transaction)

	transactions.append(transaction)

	return account_balance

def withdraw(amount, account_balance, transactions):

	if (account_balance > amount):

		account_balance -= amount

		transaction = f"Withdrew: N{amount} | New Balance: N{account_balance}"

		print(transaction)
		
		transactions.append(transaction)

	else:
		print("Withdrawal failed: insufficient funds")

	return account_balance

def show_transaction (transactions):

	print("Transactions so far: ")

	if len(transactions) > 0:

		for transaction in transactions:

			print(transaction)

	else:
		print("No transactions yet!")

