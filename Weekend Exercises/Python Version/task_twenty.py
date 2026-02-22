first_number = 0
second_number = 1

print(f"{first_number} {second_number} ", end = "")

for value in range(18):

	next_number = first_number + second_number
	first_number = second_number
	second_number = next_number
	
	print(next_number, end = " ")

print()