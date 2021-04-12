#Functions - Dice App
import random

print("Welcome to Dice App")

#intializing the DEF function
def dice(a,b):
	dice_list=[]
	for i in range(1,b+1):
		dice_sides=random.randint(1,a)
		print(f'\t{dice_sides}')
		dice_list.append(dice_sides)
	return dice_list
	

active = True
while active:
#getting the value from user
	x = int(input("How many sides would you like on your dice : "))
	y = int(input('How many dice would you like to roll : '))

	print(f'You rolled {x} {y} sided dice')
	print("\n--- The Results are follows ---")
	
	#calling the function 
	new_dice = dice(x,y)
	
	choice = input("\nWould you like to roll again ? (y/n) : ").lower()
	if choice != 'y':
		active=False
		print("Thanks for Playing the game !!!")
		break
	else:
		active=True
