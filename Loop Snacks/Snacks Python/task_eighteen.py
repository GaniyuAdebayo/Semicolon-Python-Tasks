user_number = int(input("Enter a number: "))

total = 0

while (user_number != 0):

	total += user_number%10
	user_number //= 10


print(f"The sum of the digits is {total}")