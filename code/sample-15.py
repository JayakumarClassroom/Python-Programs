import random

rand_num = random.randint(1,10)
count = 0
guess_num = 0

while guess_num !=rand_num:
	guess_num = int(input("Enter your Guess number : "))
	count+=1
	if (rand_num == guess_num):
		print("Correctly Guessed")
	elif (rand_num > guess_num):
		print("Your Guess if low")
	elif (rand_num < guess_num):
		print("Your Guess is High")
	else:
		print("Invalid Input")
print(f"It took {count} count to guess correctly")