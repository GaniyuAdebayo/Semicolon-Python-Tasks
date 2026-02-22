word = input("Enter a word: ")
new_word = ""

for letter in word:
	new_word = letter + new_word

if (word == new_word):

	print(f"{word} is a palindrome")
else:

	print(f"{word} is not a palindrome")