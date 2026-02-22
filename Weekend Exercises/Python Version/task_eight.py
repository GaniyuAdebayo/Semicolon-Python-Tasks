number = int(input("Enter a number: "))

print("The divisors are ", end = "")
for value in range(1, number+1):

	if (number % value == 0):

		print(value, end = " ")