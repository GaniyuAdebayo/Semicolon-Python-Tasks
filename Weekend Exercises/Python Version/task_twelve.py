number = int(input("Enter a number: "))

power = int(input("Enter the power: "))

result = 1

for val in range (1, power + 1):

	result *= number

print(f"{number} to power {power} is {result}")