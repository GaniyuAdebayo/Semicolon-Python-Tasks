

def digit_removal(word):

	if (type(word) != str):

		raise TypeError ("Argument is not a string")

	word = str(word)
	new_word = ""
	counter = 1

	for letter in word:
		
		if counter % 2 == 0:
			new_word += letter

		counter +=1

	return new_word
