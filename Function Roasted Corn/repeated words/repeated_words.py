
def repeated_words(word, times):

	new_word = ""

	if (type(word) == str and (type(times) == int or type(times) == float)):
		if (type(times) == float):

			new_word = word

		elif (type(times) == int):

			new_word = times * word

	else:

		raise TypeError("Incorrect arguments, use (word, times)")

	return new_word
	