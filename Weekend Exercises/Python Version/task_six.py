word = input("Enter a word")

print("Letter ASCII Value")

for letter in word:

	print(f"{letter: >3} {ord(letter): >10}")