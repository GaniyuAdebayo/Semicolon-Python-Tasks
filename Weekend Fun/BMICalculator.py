

weight = float(input("Insert your weight (kg): "))
height = float(input("Input your height (m): "))

BMI = weight / (height ** 2)

if (BMI >= 30.0):
	print("Obese")
elif (BMI >= 25.0):
	print("Overweight")
elif (BMI >= 18.5):
	print("Normal")
else:
	print("Underweight")