number = int(input("Enter a number: "))

binary_number = ""

while (number != 0):

	binary_number = str(number % 2) + binary_number
	number //= 2

print("The base 2 equivalent is", binary_number)