word = input("Enter a word: ")
new_word = ""
for letter in word:
	new_word += letter.upper()

print(new_word)