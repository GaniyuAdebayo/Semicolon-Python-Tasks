user_number = int(input("Enter a number: "))

smallest = user_number % 10

while (user_number != 0):

	if (user_number % 10 < smallest):

		smallest = user_number % 10

	user_number //= 10


print(f"The largest of the digits is {smallest}")