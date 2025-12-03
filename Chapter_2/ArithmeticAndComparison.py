

#Exercise 2.10

#request for first, second and third number from user and store in first_number, second_number, and third_number respectively
#Evaluate the sum by adding first_number, second_number and third_number, store the result in "sum"
#evaluate average by dividing sum by 3
# evaluate the product of the three numbers and store in "product"
#to obtain largest number of the three numbers, assume first_number as the largest and store in 'largest'
#if second_number is greater than largest, assign second_number to largest
#if third_number is greater than largest, assign third_number to largest
#to obtain smallest number of the three numbers, assume first_number as the smallest and store in 'smallest'
#if second_number is less than smallest, assign second_number to smallest
#if third_number is less than smallest, assign third_number to smallest
#output sum, average, product, largest and smallest


first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
third_number = int(input("Enter third number: ")) 

sum = first_number + second_number + third_number
average = sum/3
product = first_number * second_number * third_number

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


print("The sum, average and products of the numbers are", sum, ",", round(average, 2), ", and", product, "respectively")
print("The greatest and smallest numbers are", largest, "and", smallest, "respectively")

