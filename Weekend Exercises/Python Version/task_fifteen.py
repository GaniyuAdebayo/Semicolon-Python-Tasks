number = int(input("Enter a number: "))

sum = 0
while (number != 0):

	if ((number % 10) % 2 != 0):

		sum += (number % 10)

	number //= 10

print("The sum of the odd digits is", sum)