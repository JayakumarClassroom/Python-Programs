#Conditional Loop - Coin Toss program
import random

print("Welcome to Coin Toss App")

flip_num = int(input("\nHow many time do you like to flip a coin ? "))
choice = input("\nwould you like to see the result of each flip (Y/N) : ").lower()

heads = 0
tails = 0

for flips in range(flip_num):
	#create the coin object
	coin = random.randint(0,1)
	
	if coin ==1:
		heads += 1
		if choice.startswith('y'):
			print("HEADS")
	else:
		tails +=1
		if choice.startswith('y'):
			print("TAILS")
		
	if heads == tails: 
		print("At " + str(flips+1) + " flips, the number of heads and tails were equal at " + str(heads) + " each.")

#Calculate the percentage 
heads_percentage = round(100 * heads /flip_num,2)
tails_percentage = round(100 * tails /flip_num,2)

#Final Result Display 

print(f"\nResults of flipping a coin {flip_num} Times : ")
print("\nSides \t\tCount\t\tPercentage")
print(f"Heads {heads} \t {flip_num} \t\t {heads_percentage}")
print(f"Tails {tails} \t {flip_num} \t\t {tails_percentage}")