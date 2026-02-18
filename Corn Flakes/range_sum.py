
sum = 0

for val in range (10, 20001, 10):

	sum += val

print(f"The sum of multiples of 10 from 1 to 20000 is {sum}")
	


for val in range (1, 16):

	print(val * 3)



for val in range (1, 100):

	if (val % 2 == 0):

		print(val, end = " ")

print()



passes = 0

for val in range (1, 16):

	score = float(input(f"Enter score {val}:"))

	if (score >= 45):

		passes += 1

print(f"Pass: {passes}")
print(f"Fail: {15 - passes}")



table_num = int(input("Enter table number: "))

for val in range (1, 11):

	print(f"{table_num} X {val} = {table_num * val}")



triangle_height = int(input("Enter the triangle height:"))

for val in range (triangle_height + 1):

	for value in range (val + 1):

		print("*", end = "")

	print()


for val in range (5, 0, -1):

	for value in range (val, 0, -1):

		print(value, end = " ")

	print()



height = int(input("Enter triangle height: "))
for val in range (height):

	for value in range (val + 1):

		print("*", end = "")

	print()
print()


for val in range (height, 0, -1):

	for value in range (val):

		print("*", end = "")

	print()
print()

	
for val in range (height, 0, -1):

	for value in range (height - val):

		print(" ", end = "")

	for values in range (val):

		print("*", end = "")

	print()
print()


for val in range (height, 0, -1):

	for value in range (val - 1):

		print(" ", end = "")

	for values in range (height - val + 1):

		print("*", end = "")

	

	print()
