import math
menu_choice = """

	Welcome to Iya Scambirah Pizza Joint Ajegunle

	Pizza Type	Number of Slices	Price Per Box

	Sapa Size		4				2000
	Small Money		6				2400
	Big Boys		8				3000
	Odogwu			12				4200

	"""

print(menu_choice)

pizza_type = input("Enter type of pizza: ")

match (pizza_type):

	case ("Sapa Size"):
		number_of_slices = 4
		price_per_box = 2000

	case ("Small Money"):
		
		number_of_slices = 6
		price_per_box = 2400

	case ("Big Boys"):
	
		number_of_slices = 8
		price_per_box = 3000

	case ("Odogwu"):

		number_of_slices = 12
		price_per_box = 4200

	case _:

		print(f"{pizza_type} not available!")

guests_number = int(input("Enter number of guests: "))

number_of_pizza_to_buy = math.ceil(guests_number / number_of_slices)

total_price = number_of_pizza_to_buy * price_per_box

pizza_slices_left = (number_of_pizza_to_buy * number_of_slices) - guests_number


print(f"\nNumber of boxes of pizza to buy: {number_of_pizza_to_buy}\n")
print(f"Number of left over slices after serving = {pizza_slices_left} slices\n")
print(f"Price of {number_of_pizza_to_buy} boxes = {total_price}\n")

		