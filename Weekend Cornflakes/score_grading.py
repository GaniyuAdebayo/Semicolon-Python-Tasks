
counter = 1
n_fail = 0
n_pass = 0

while (counter <= 15):

	score = int(input("Enter score: "))

	if(score >= 25):
		print("Pass")
		n_pass += 1
	else:
		print("Fail")
		n_fail += 1

	counter +=1

print("Pass: ", n_pass, "\nFail: ", n_fail)