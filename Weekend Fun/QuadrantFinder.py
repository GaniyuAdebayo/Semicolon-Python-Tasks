
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

if (x > 0 & y > 0):
	print("Q1")
if (x < 0 & y > 0):
	print("Q2")
if (x < 0 & y < 0):
	print("Q3")
if (x > 0 & y < 0):
	print("Q4")
if (x == 0 & y == 0):
	print("Origin")
if (x != 0 & y ==0):
	print("X-axis")
if (x == 0 & y!= 0):
	print("Y-axis")