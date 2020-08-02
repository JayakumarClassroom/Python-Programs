'''
Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:
	Rock beats scissors 
	Scissors beats paper
	Paper beats rock
'''
def rockPaperscissors():
	user_Input_1 = input("Enter the Player 1 input : ").lower()
	user_Input_2 = input("Enter the Player 2 input : ").lower()
	#Rock = r
	#Scissor = s
	#paper = p
	if (user_Input_1=='rock' and user_Input_2=='scissors'):
		print("User-1 Rock Wins")
	elif (user_Input_1=='scissors' and user_Input_2=='rock'):
		print("User-2 Rock Wins")
	elif (user_Input_1=='scissors' and user_Input_2=='paper'):
		print("User-1 Scissor Wins")
	elif (user_Input_1=='paper' and user_Input_2=='scissor'):
		print("User-2 Scissor Wins")
	elif (user_Input_1=='paper' and user_Input_2=='rock'):
		print("User-1 paper Wins")
	elif (user_Input_1=='rock' and user_Input_2=='paper'):
		print("User-2 paper Wins")
	else:
		print("Invalid Input")
	
	playAgain()

def playAgain():
	again = input("Would you like to play again?  Enter Y for yes, N for no ")
	if again == "Y" or again== "y":
		rockPaperscissors()
	elif again == "N" or again== "n":
		print ("Thanks for playing!")
rockPaperscissors()