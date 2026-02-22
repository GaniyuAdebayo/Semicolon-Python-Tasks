number = int(input("Enter a number"))

new_number = str(number)

reversed_number = ""

for num in new_number:

	reversed_number = num + reversed_number

print(reversed_number)