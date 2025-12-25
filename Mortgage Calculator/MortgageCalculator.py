
principal = float(input("Enter the principal amount: "))

rate = float(input("Enter the annual interest rate: "))

years = int(input("Enter the duration in years: "))

rate = rate / (100 * 12)

months = years * 12

exponential = (1 + rate) ** months

monthly_payment = principal * rate * exponential * (1 / (exponential - 1))

print(f"Your monthly payment is ${monthly_payment:.2f}")