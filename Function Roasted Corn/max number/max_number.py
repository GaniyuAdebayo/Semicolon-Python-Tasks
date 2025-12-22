def max_number(word):

	largest = word[0]

	for number in range(0, len(word)):

		if (type(word[number]) != int):

			raise TypeError ("list contains non-numeric value")

	for counter in range(1, len(word)):

		if (word[counter] > largest):

			largest = word[counter]

	return largest


