sentence = input("Enter a sentence: ").strip()

count = 1

for value in range(len(sentence)):

	if (sentence[value] == " "):
		count += 1

	if (sentence[value] == " " and sentence[value + 1] == " "):

		count -= 1

print("The number of words is", count)