user_number = int(input("Enter a number: "))

count = 0

while (user_number != 0):

	user_number //= 10

	count += 1

print(f"The number of digits is {count}")