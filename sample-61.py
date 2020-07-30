#While Loop - Power ball Simulator App or Lottery Ticket Generator App
import random

print("Welcome to Power ball Simulator App or Lottery Ticket Generator App")

#Get input from user for White and Red Balls
white_balls = int(input("How many White balls to Draw (Min of 5 and Max of 69 :"))
if white_balls <= 5 or white_balls >69:
	white_balls=random.randint(5,69)
#print(white_balls)

red_balls = int(input("How many Red balls to Draw (Min of 1 and Max of 26 :"))
if red_balls < 1 or red_balls >26:
	red_balls=random.randint(2,26)
#print(red_balls)

#Generating the chances of winning the ticket
odds =1
for i in range(5):
	odds *= white_balls +1
odds = round((odds * red_balls)/120)
print(f"\nYou have a 1 in {odds} chance of winning the tickets.")

purchase_ticket = int(input("How many tickets do you like to purchase ? "))

winning_interval = []
#for white balls
while len(winning_interval)<5:
	number=random.randint(1,white_balls)
	if number not in winning_interval:
		winning_interval.append(number)

#sorting the number
winning_interval.sort()

#for red balls
number = random.randint(1,red_balls)
winning_interval.append(number)


#Simulate powerball game 

print("\nWelcome to Power ball Simulator App or Lottery Ticket Generator App ")
print("\nTonight Winning numbers are : ",end='')
for number in winning_interval:
	print(f'{number}', end=' ')
	
	
input("\n\nPress 'ENTER' Key to begin purchase")

new_purchase_ticket=0
active = True
ticket_sold = []

#Run if yo have not purchased the ticket 
while winning_interval not in ticket_sold and active == True:
	#make a lottery ticket to buy
	lotter_number=[]
	
	#for white balls
	while len(lotter_number) < 5:
		number = random.randint(1,white_balls)
		if number not in lotter_number:
				lotter_number.append(number)
	lotter_number.sort()
	
	#for red balls
	number = random.randint(1,red_balls)
	lotter_number.append(red_balls)
	
	#This current ticket not yet sold
	
	if lotter_number not in ticket_sold:
		new_purchase_ticket += 1
		ticket_sold.append(lotter_number)
		print(lotter_number)
	else:
		print("Losing ticket generated........")
	
	#Ask user for more tickets or not
	if new_purchase_ticket % purchase_ticket == 0:
		print(str(new_purchase_ticket) + ' ticket purchased so far NO Winner :(....')
		choice = input("Do you want continue buying tickes ? (Y/N) : ")
		if choice != 'y':
			active= False
			print("Thanks for playing .....")

#The lottery is not over
#Purchased the winning lottery, we won the lottery 

if lotter_number == winning_interval:
	print("\nWinning Ticket Number is : ",end ='')
	for number in lotter_number:
		print(str(number),end=' ')
	print("\nPurchased a total of " + str(new_purchase_ticket) + " tickets.")
else:
	print(f"\nYou bought {new_purchase_ticket} tickets and still lost..")
	print("Better luck next time...!")