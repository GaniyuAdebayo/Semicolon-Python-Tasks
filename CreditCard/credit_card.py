import re

def card_number_length(number):

	number = str(number)
	
	card_length = credit_card_number(number)

	return card_length

def credit_card_type(number):

	number = str(number)

	number = credit_card_number(number)

	type = ""

	if (number.startswith("4")):
		type = "Visa Card"
	
	elif (number.startswith("5")):
		type = "Master Card"

	elif (number.startswith("6")):
		type = "Discover Card"
	
	elif (number.startswith("37")):
		type = "American Express Card"
	else:
		type = "Invalid Card"

	return type


def credit_card_number(number):

	number = str(number)
	
	numberOnly = re.match("^[\\d\\s-]{13,19}$", number)		

	number = re.sub("\\D+", "", number)	

	if (len(number) >= 13 and len(number) <= 16 and numberOnly != None):

		return number
	else:
		raise RuntimeError("Invalid Number, please try again")


def credit_card_validity_status (number):

	number = str(number)

	number = credit_card_number(number)

	evenSum = 0
	oddSum = 0


	for value in range (1, len(number) + 1):

		if (value % 2 == 0):

			val = int(number[len(number) - value]) * 2

			if (val > 9):
				evenSum += (val - 9)
			
			else:
				evenSum += val

		else:

			oddSum = oddSum + int(number[len(number) - value])


	if ((evenSum + oddSum) % 10 == 0):
		return "Valid"
	else:
		return "Invalid"
