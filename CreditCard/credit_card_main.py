from credit_card import * 


number = input("Hello, Kindly Enter Card details to verify: ")

print(f"Credit Card Type: {credit_card_type(number)}")
print(f"Credit Card Number: {credit_card_number(number)}")
print(f"Credit Card Digit Length: {card_number_length(number)}")
print(f"Credit Card Validity Status: {credit_card_validity_status(number)}")



