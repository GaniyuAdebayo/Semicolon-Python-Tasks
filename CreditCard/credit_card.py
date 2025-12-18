import re

def card_number_length(number):
	
	card_length = len(number)

	return f"Credit Card Number Length: {card_length}"

def credit_card_type(number):

	if (number.startswith("4")):
		return ("Credit Card Type: Visa Card")
	
	elif (number.startswith("5")):
		return ("Credit Card Type: Master Card")

	elif (number.startswith("6")):
		return ("Credit Card Type: Discover Card")
	
	elif (number.startswith("37")):
		return ("Credit Card Type: Master Card")
	else:
		return ("Credit Card Type: Invalid Card")

def credit_card_number(number):

	return (f"Credit Card Number: {number}")

def credit_card_validity_status (number):

	for value in range (1, len(number) + 1):

		evenSum = 0
		oddSum = 0
		if (value % 2 == 0):

			evenSum = (int(number[len(number) - value]) * 2) + evenSum 

		else:

			oddSum = oddSum + int(number[len(number) - value])

	if ((evenSum + oddSum) % 10 == 0):
		return "Credit Card Validity Status: Valid"
	else:
		return "Credit Card Validity Status: Invalid"
