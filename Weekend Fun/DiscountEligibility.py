
total_bill = float(input("Input your total bill: "))
is_member = input("Are you a member? Yes/No")

if (total_bill >= 1000 and (is_member == "Yes" or is_member == "yes" or is_member == "YES")):
	print("Your bill after 10% discount is", round((0.9 * total_bill), 2))
elif (total_bill >= 1000 and (is_member == "No" or is_member == "no" or is_member == "NO")):
	print("Your bill after 5% discount is", round((0.95 * total_bill), 2))
else:
	print("No discount")