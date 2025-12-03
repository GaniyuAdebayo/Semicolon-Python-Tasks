

#Exercise 2.14

#collect the age of user and store in "age"
#obtain the maximum heart rate using the expression below
#max_heart_rate = 200 - age
#obtain min and max of the target heart rate by multiplying with 0.5 and 0.85 respectively 



age = int(input("Enter your age: "))

max_heart_rate = 200 - age

min_target_heart_rate = max_heart_rate * 0.5
max_target_heart_rate = max_heart_rate * 0.85


print("Your maximum heart rate is", max_heart_rate, ", kindly target between", min_target_heart_rate, "and", max_target_heart_rate)
