
import re

def word_slicing(word):

	if (type(word) != str):

		raise TypeError("Input is not a string")
	
	word = re.sub(" ", "", word)

	newWord = ""
	if (len(word) >= 4):

		newWord = word[0] + word[1] + word[len(word) - 2] + word[len(word)-1]
		
	
	elif (len(word) >= 2):
		newWord = 2 * (word[0] + word[len(word) - 1])

	elif (len(word) <= 1):
		newWord = ""

	else:
		newWord = ""

	return newWord.lower()
