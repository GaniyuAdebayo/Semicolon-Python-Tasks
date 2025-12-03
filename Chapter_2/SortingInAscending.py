
#Exercise 2.15

first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
third_number = int(input("Enter third number: ")) 

largest = first_number

if (second_number > largest):
	largest = second_number
if (third_number > largest):
	largest = third_number

smallest = first_number

if (second_number < smallest):
	smallest = second_number
if (third_number < smallest):
	smallest = third_number

if (first_number == largest & second_number == smallest):
	print(second_number, third_number, first_number)
elif (first_number == largest & third_number == smallest):
	print(third_number, second_number, first_number)
elif (second_number == largest & first_number == smallest):
	print(first_number, third_number, second_number)
elif (second_number == largest & third_number == smallest):
	print(third_number, first_number, second_number)
elif (third_number == largest & first_number == smallest):
	print(first_number, second_number, third_number)
else:
	print(second_number, first_number, third_number)

