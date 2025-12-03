

#Exercise 2.11

#collect a 5 digit number and store in "number"
#make floor division of number with 10000 and store in "ten_thousand"
#make floor division of the remainder of ten_thousand with 1000 and store in "thousand"
#make floor division of the remainder from thousand with 100 and store in "hundred"
#make floor division of the remainder from hundred with 10 and store in "ten"
#obtain the remainder from ten and store in "unit"
#print out ten_thousand, thousand, hundred, ten, unit on the same line




number = int(input("Enter a 5 digit number: "))

ten_thousand = number // 10000
thousand = (number % 10000) // 1000
hundred = ((number % 10000) % 1000) // 100
ten = (((number % 10000) % 1000) % 100) //10
unit = (((number % 10000) % 1000) % 100) % 10

print(ten_thousand, "\t", thousand, "\t", hundred, "\t", ten, "\t", unit)

