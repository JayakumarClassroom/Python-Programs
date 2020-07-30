#conditional statement - Guess My Number App

import random

print("Welcome to Guess My Number App")

name = input("Enter your name to play : ").title()
print(f'Welcome {name}!, I am thinking of a number between 1 and 20.')

#conditional statement for play
count = 0
number= random.randint(1,20)
for i in range(5):
	guess = int(input("Take a Guess : "))
	if number > guess:
		print("Your Guess is Low")
		count +=1
	elif number < guess:
		count +=1
		print("Your Guess is High")
	else:
		break

if guess == number:
	print(f"\nGood Job, {name}! You guessed my number in {count+1} guesses! ")
else:
	print(f'\nGame Over. The number I was thinking of was {number}')		
		