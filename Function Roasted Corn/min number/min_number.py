
def min_number(word):

	for number in range (0, len(word)):

		if (type(word[number]) != int):

			raise TypeError("List contains non-numeric value")

	minimum = word[0]

	for counter in range(1, len(word)):

		if (word[counter] < minimum):

			minimum = word[counter]

	return minimum
