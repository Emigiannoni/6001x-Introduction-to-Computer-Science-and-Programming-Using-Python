# Test Case 1:
balance = 3329
annualInterestRate = 0.2
months = 12

new_balance = balance

payment = 0

def calculate_new_balance(new_balance, payment, annualInterestRate):

	return (new_balance - payment) + ((new_balance - payment) * annualInterestRate / 12)

while new_balance > 0:

	new_balance = balance

	payment += 10

	for i in range(months):

		new_balance = calculate_new_balance(new_balance, payment, annualInterestRate)

 
print('Lowest Payment: ' + str(payment))