
def continuous_noun(word):

	new_word = ""

	if (word.isalpha()):

		if (len(word) >= 3):

			if (word.endswith("ing")):

				new_word = word + "ly"
			else:
				new_word = word + "ing"

		else:
			new_word = word

	else:

		raise TypeError ("Word contains non-literal")

	

	return new_word
