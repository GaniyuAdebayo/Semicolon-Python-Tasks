number = input("Enter a binary number (1s and 0s only): ")

count = 0

number_integer = int(number)
decimal_number = 0

while (number_integer != 0):

	decimal_number += ((number_integer % 10) * (2 ** count))
	number_integer //= 10
	count += 1

print("The base 10 equivalent is", decimal_number)