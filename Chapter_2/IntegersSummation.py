
number_of_integers = int(input("How many integers are you inputing: "))

print("Enter your integers: ")


counter = 1
oddSum = 0
evenSum = 0

while (counter <= number_of_integers):

	number = int(input())

	if (number%2 == 0):
		evenSum += number
	else:
		oddSum += number
	counter += 1

print("The sum of odd numbers and sum of even numbers are", oddSum, "and", evenSum, "respectively")