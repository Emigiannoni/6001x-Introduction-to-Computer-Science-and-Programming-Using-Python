# Test Case 1:
balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
months = 12

def minimum_payment(monthlyPaymentRate, balance):

	return balance * monthlyPaymentRate

def interest(annualInterestRate, balance):

	return (annualInterestRate / 12) * balance


for i in range(months):

	unpaid_balance = balance - minimum_payment(monthlyPaymentRate, balance)

	balance = unpaid_balance + interest(annualInterestRate, unpaid_balance)

print('Remaining balance: ' + str(round(balance, 2)))





