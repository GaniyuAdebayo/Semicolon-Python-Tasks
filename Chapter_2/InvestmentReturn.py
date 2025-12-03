

#Exercise 2.12

#initialize rate, principal, year as 10 years, 20 years and 30 years as 0.07, 1000, 10, 20, and 30 respectively
#evaluate the amount from 10 years, 20 years and 30 years using the expression provided



rate = 0.07
principal = 1000
year_10 = 10
year_20 = 20
year_30 = 30

amount_10 = principal * ((1 + rate)**year_10)
amount_20 = principal * ((1 + rate)**year_20)
amount_30 = principal * ((1 + rate)**year_30)

print("The amount at the end of year 10 is", round(amount_10, 2))
print("The amount at the end of year 20 is", round(amount_20, 2))
print("The amount at the end of year 30 is", round(amount_30, 2))

