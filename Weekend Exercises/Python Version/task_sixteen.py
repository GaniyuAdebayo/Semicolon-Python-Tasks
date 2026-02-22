for value in range(1, 101):

	count = 0

	half_number = 0

	if (value % 2 == 0):
		half_number = value //2
	else:
		half_number = value//2 + 1

	for val in range (1, half_number + 1):

		if (value % val == 0):
			count += 1
	
	if (count == 1 and value != 1):
		print(value, end = " ")

print()