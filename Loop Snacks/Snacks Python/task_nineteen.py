user_number = int(input("Enter a number: "))

largest = user_number % 10

while (user_number != 0):

	if (user_number % 10 > largest):

		largest = user_number % 10

	user_number //= 10


print(f"The largest of the digits is {largest}")