word = input("Enter a word: ")
new_word = ""
for letter in word:
	new_word += letter.lower()

print(new_word)