

number1 = int(input("Insert first number: "))
number2 = int(input("Insert second number: "))
number3 = int (input("Insert third number: "))

largest = number1

if (number2 > largest):
	largest = number2
if (number3 > largest):
	largest = number3

print("The largest number is", largest)