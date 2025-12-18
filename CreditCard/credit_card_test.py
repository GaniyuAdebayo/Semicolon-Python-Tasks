from credit_card import * 
import re


number = input("Enter Card Number: ")

numberOnly = re.match("^[\\d\\s-]{16,19}$", number)

print(numberOnly)

if (numberOnly == None):

	raise RuntimeError("Invalid Number, please try again")

number = re.sub("\\D+", "", number)

if (len(number) >= 13 and len(number) <= 16):
	print(credit_card_type(number))
	print(credit_card_number(number))
	print(card_number_length(number))
	print(credit_card_validity_status(number))


