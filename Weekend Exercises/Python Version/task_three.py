word = input("Enter a word: ")

count = 0

for letter in word:

	if (letter.isupper()):
		count += 1

print("Number of upper case is", count)