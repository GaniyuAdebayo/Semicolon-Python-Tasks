def sum_of_range (first_num, last_num, multiple):

	sum = 0
	
	while (first_num % multiple != 0):

		first_num += 1

	for val in range (first_num, last_num + 1, multiple):

		if(val % multiple == 0):

			sum += val

	return sum


def multiples_of_three (num_of_val):

	for val in range (1, num_of_val):

		print (val)

def even_values (start, end):

	for val in range (start, end + 1):

		if (val % 2 == 0):

			print(val, end = " ")

	print()

def score_grader(num_of_students):

	passes = 0

	for val in range (1, num_of_students):

		score = float(input(f"Enter score {val}:"))

		if (score >= 45):

			passes += 1

	print(f"Pass: {passes}")
	print(f"Fail: {num_of_students - passes}")

def multiplication_table (table_num):

	for val in range (1, 11):

		print(f"{table_num} X {val} = {table_num * val}")


def triangle(triangle_height):

	for val in range (triangle_height + 1):

		for value in range (val + 1):

			print("*", end = "")

		print()

def number_triangle(beginning_num):

	for val in range (beginning_num, 0, -1):

		for value in range (val, 0, -1):

			print(value, end = " ")

		print()

def var_triangle(height):

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

	print()