word = input("Enter a word: ")

count = 1

for letter in word.lower():

	if (letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u"):

		break;

	count += 1;

print("The position of first vowel is", count)
