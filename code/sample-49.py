#conditional statment - Rock, Paper and Scissors
import random

print('Welcome to the Game Rock, Paper and Scissors')

#Choose the number of rounds
rounds = int(input("\nHow many rounds do you like to play ? "))

#initialize Zero for both player and computer
player=0
computer=0

#list the moves
moves = ["Rock", "Paper", "Scissor"]

#The looping function for game
for i in range(1,rounds+1):
	print(f'\nRound : {i}')
	print(f"Player : {player}   Computer: {computer}")
	
	#Computer randomly choosing the moves
	c_index = random.randint(0,2)
	c_choice = moves[c_index]
	
	#Player choosing the moves
	p_choice = input("Time to Pick up ... Rock / Paper / Scissor : ").title()
	
	if p_choice in moves:
		print(f'\tComputer : {c_choice}')
		print(f'\tPlayer   : {p_choice}')
		
		#choosing the moves using conditional statements
		
		#computer chooses ROCK
		if p_choice == 'Rock' and c_choice == 'Rock':
			winner = 'tie'
			phrase = 'Its a tie, how boring'
		
		elif p_choice == 'Paper' and c_choice == 'Rock':
			winner = 'player'
			phrase = 'Paper covers Rock'
		
		elif p_choice == 'Scissor' and c_choice == 'Rock':
			winner = 'computer'
			phrase = 'Rock smashes Scissor'
		
		#computer chooses PAPER
		elif p_choice == 'Paper' and c_choice == 'Paper':
			winner = 'tie'
			phrase = 'Its a tie, how boring'
		
		elif p_choice == 'Rock' and c_choice == 'Paper':
			winner = 'computer'
			phrase = 'Paper covers Rock'
		
		elif p_choice == 'Scissor' and c_choice == 'Paper':
			winner = 'player'
			phrase = 'scissor cut paper'
	
		#computer chooses SCISSOR
		elif p_choice == 'Paper' and c_choice == 'Scissor':
			winner = 'computer'
			phrase = 'scissor cut paper'
		
		elif p_choice == 'Rock' and c_choice == 'Scissor':
			winner = 'player'
			phrase = 'Rock smashes Scissor'
		
		elif p_choice == 'Scissor' and c_choice == 'Scissor':
			winner = 'tie'
			phrase = 'Its a tie, how boring'
		
		else:
			print('Round Winner Not Calculated ')
			winner = 'tie'
		
		#Calculation of winner
		if winner == 'player':
			player +=1
			print(f'\t{phrase}')
			print(f'\tPlayers wins round {i}')
		else:
			computer+=1
			print(f'\t{phrase}')
			print(f'\tComputer wins round {i}')
	
	else:
		print("That is not a valid option. \nComputer gets the point")
		computer+=1

#final result 

print('\nFinal Game Result:')
print(f'\tRounds Playes : {rounds}')
print(f'\tPlayer Score : {player}')
print(f'\tComputer Score : {computer}')

if player > computer:
	print("\tPLAYER Wins!!!!")
elif player < computer:
	print("\tComputer Wins!!!!")
else:
	print("\tThe Game was a tie.")
	