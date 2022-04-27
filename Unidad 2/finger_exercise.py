print("Please think of a number between 0 and 100!")

high = 100

low = 0

mid = high // 2

print("Is your secret number " + str(int(mid)) + "?")

answer = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")

while answer != 'c':

	if answer == 'h':

		high = mid

	elif answer == 'l':

		low = mid

	else:

		print("Sorry, I did not understand your input.")


	mid = low + ((high - low) // 2)

	print("Is your secret number " + str(int(mid)) + "?")

	answer = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")

print("Game over. Your secret number was: " + str(int(mid)))




