

def number_squared(number):

	for value in number:

		if (type(value) != int):
			raise TypeError("Non-integer value contained in the list")

	new_number = []

	for values in number:

		new_number.append(values ** 2)

	return new_number
