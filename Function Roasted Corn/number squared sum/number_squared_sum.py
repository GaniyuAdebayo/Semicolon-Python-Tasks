

def number_squared_sum(number):

	for value in number:

		if (type(value) != int):
			raise TypeError("Non-integer value contained in the list")

	sum = 0

	for values in number:

		sum += (values ** 2)

	return sum