#Functions - Dice App 
import random

def dice_sides():
	#Ask user how many sides on their dice
	sides = int(input("How many sides would you like on your dice : "))
	return sides
	
def dice_numbers():
	#Ask user how many time roll the dice
	number = int(input('How many dice would you like to roll : '))
	return number


def dice_roll(sides, number):
	#simulate rolling the dice
	dice_list=[]
	print(f'You rolled {number} {sides} sided dice.')
	print("\n--- The Results are follows ---")
	for i in range(1,number+1):
		dice_sides=random.randint(1,sides)
		print(f'\t{dice_sides}')
		dice_list.append(dice_sides)
	return dice_list

def dice_sum(dice_list):
	#add all the value of dice
	
	#using built-in sum function
	#print(f'The Total value of your roll is {sum(dice_list)}.')
	
	#manual way to sum
	total = 0
	for dice in dice_list:
		total += dice	
	print(f'The Total value of your roll is {total}.')
	

def roll_again():
	#ask the user to roll again 
	
	active = True
	choice = input("\nWould you like to roll again ? (y/n) : ").lower()
	if choice != 'y':
		active = False
		print("Thanks for Playing the game !!!")
	else:
		active = True
	return active
	
#Main code
print("Welcome to Dice App")

rolling = True
while rolling:
	#get the dice info 
	d_sides = dice_sides()
	d_number = dice_numbers()
	
	#roll the dice
	d_roll = dice_roll(d_sides, d_number)
	dice_sum(d_roll)
	
	#roll again
	rolling = roll_again()

print("Thank you for using the Print Dice")