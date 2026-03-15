import random
def randomNumbers():

	list_of_numbers = []
	for value in range(10):
		list_of_numbers.append(random.randInt(1, 50))
	return list_of_numbers

def length_of_list(numbers):

	count = 0
	for _ in numbers:
		count += 1
	return count

def sum_of_elements_at_even_positions(numbers):

	total = 0
	count = 1	
	for value in numbers:
		if (count % 2 == 0):
			total += value
		count += 1
	return total

def sum_of_elements_at_odd_positions(numbers):

	total = 0
	count = 1	
	for value in numbers:
		if (count % 2 != 0):
			total += value
		count += 1
	return total

def product_of_elements_in_every_third_positions(numbers):

	product = 1
	count = 1	
	for value in numbers:
		if (count % 3 == 0):
			product *= value
		count += 1
	return product

def average_of_elements(numbers):

	total = 0.0;
	for value in numbers:
		total += value

	return total/length_of_list(numbers)

def largest_element(numbers):

	largest = numbers[0]
	for value in numbers:
		if (value > largest):
			largest = value

	return largest

def smallest_element(numbers):

	smallest = numbers[0]

	for value in numbers:
		if (value < smallest):
			smallest = value
	return smallest

def string_length_in_a_list(list_of_string):
	
	no_of_strings = length_of_list(list_of_string)
	unique_string = []

	for value in list_of_string:

		if (length_of_list(value) >= 2 and value.lower()[0] == value.lower()[length_of_list(value) - 1]):
			unique_string.append(value)

	return no_of_strings, unique_string

def list_of_integers():

	integers = []
	for val in range(1, 16):

		integers.append(val)

	print(integers)

	return integers

def sum_of_elements_at_multiples_of_three(numbers):

	total = 0

	count = 1

	for number in numbers:

		if (count % 3 == 0):

			total += number
		count += 1

	return total

def sum_of_elements_in_first_middle_and_last_position(numbers):

	sum = numbers[0] + numbers[len(numbers) - 1]

	if (len(numbers) % 2 != 0):

		sum += numbers[len(numbers) // 2]

	else:

		sum += (numbers[len(numbers) // 2] + numbers[(len(numbers) // 2) - 1])/2

	return sum
			

