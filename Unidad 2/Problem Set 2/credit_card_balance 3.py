balance = 320000
annualInterestRate = 0.2

interest_rate = (annualInterestRate) / 12.0
payment_lower = balance / 12
payment_upper = (balance * (1 + interest_rate)**12) / 12.0
payment_mid = (payment_upper + payment_lower) / 2

non_paid = balance

while abs(non_paid) > 0.01:

	non_paid = balance

	for i in range(12):

		non_paid = non_paid - payment_mid

		non_paid = non_paid * (1 + interest_rate) 

	if non_paid > 0:

		payment_lower = payment_mid

		payment_mid = (payment_upper + payment_lower) / 2


	elif non_paid < 0:

		payment_upper = payment_mid

		payment_mid = (payment_upper + payment_lower) / 2



print('Lowest Payment: ' + str(round(payment_mid, 2)))






