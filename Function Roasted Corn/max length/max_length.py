
def longest_word(words):
	
	longest_word = ""
	length_of_word = 0

	for value in words:
		if (type(value) != str):

			raise TypeError ("The list contains type other than String")

	for word in words:

		if (len(word) > len(longest_word)):

			longest_word = word
			length_of_word = len(word)

	return longest_word, length_of_word

