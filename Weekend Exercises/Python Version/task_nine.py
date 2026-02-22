number = int(input("Enter a number: "))

count = 0
for value in range(1, number+1):

	if (number % value == 0):

		count += 1

print("The number of divisors is", count)