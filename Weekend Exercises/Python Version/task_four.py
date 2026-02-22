word = input("Enter a word: ")

count = 0

for letter in word:

	if (letter.islower()):
		count += 1

print("Number of lower case is", count)