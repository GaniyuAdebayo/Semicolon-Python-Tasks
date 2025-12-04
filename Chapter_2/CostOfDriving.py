
distance = float(input("Enter distance travelled: "))
car_efficiency = float(input("Enter your car efficiency: "))
price = float(input("Enter the price per gallon: "))


cost_of_trip = (distance * price)/car_efficiency


print("The total cost of travel is $" + str(round(cost_of_trip, 2)))