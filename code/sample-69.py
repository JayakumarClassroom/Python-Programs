#Function - Tic Tac Toe App

def draw_board(char_list):
	#create a Tic Tac Toe board 
	print("\n\t Tic-Tac-Toe App")
	print("\t~~~~~~~~~~~~~~~~~")
	print("\t|| " + char_list[0] + " || " + char_list[1] + " || " + char_list[2] + " || ")
	print("\t~~~~~~~~~~~~~~~~~")
	print("\t|| " + char_list[3] + " || " + char_list[4] + " || " + char_list[5] + " || ")
	print("\t~~~~~~~~~~~~~~~~~")
	print("\t|| " + char_list[6] + " || " + char_list[7] + " || " + char_list[8] + " || ")
	print("\t~~~~~~~~~~~~~~~~~")


def get_player_input(player_char,char_list):
	#Get the user input to play a game and find the appropriate position for those.
	while True:
		#Get player input
		player_move = int(input("Player " + player_char + " : Where would you like to place your piece (1-9) : "))
		#move the piece to board
		if player_move > 0  and player_move < 10:
			#move the piece to an empty spot
			if char_list[player_move - 1] == '_':
				return player_move
			else:
				print("The spot already been choosen")
		else:
			print("Invalid number, The number must between (1-9) ")
		
def player_char_on_board(player_char,player_move,char_list):
		#Choosing the player to play the game
		#put a player character at the correct spot on the board
		
		char_list[player_move - 1] = player_char


def is_winner(player_char,char_list):
	return(
			(char_list[6]==player_char and char_list[7]==player_char and char_list[8]==player_char) or 
			(char_list[3]==player_char and char_list[4]==player_char and char_list[5]==player_char) or
			(char_list[2]==player_char and char_list[1]==player_char and char_list[0]==player_char) or
			(char_list[6]==player_char and char_list[4]==player_char and char_list[2]==player_char) or
			(char_list[0]==player_char and char_list[4]==player_char and char_list[8]==player_char) or
			(char_list[6]==player_char and char_list[3]==player_char and char_list[0]==player_char) or
			(char_list[7]==player_char and char_list[4]==player_char and char_list[1]==player_char) or
			(char_list[8]==player_char and char_list[5]==player_char and char_list[2]==player_char)
		)
	
	
#main code
player_1 = 'X'
player_2 = 'O'
n_list = ['1','2','3','4','5','6','7','8','9']
c_list = ['_']*9

#Display the initial state of the Tic Tac Toe App Game Board
draw_board(n_list)
draw_board(c_list)

#using while loop until player win
running = True
while running:
#player 1 turn and Get the player move
	move = get_player_input(player_1, c_list)
	#put move on board
	player_char_on_board(player_1, move, c_list)
	#Re-draw the board 
	draw_board(n_list)
	draw_board(c_list)
	if is_winner(player_1, c_list):
		print("\nPlayer 1 WINS!!!!!!")
		break
	#check if there is a tie
	elif '_' not in c_list:
		print('The game was a tie')
		break
	
	
#player 2 turn and Get the player move
	move = get_player_input(player_2, c_list)
	#put move on board
	player_char_on_board(player_2, move, c_list)
	#Re-draw the board 
	draw_board(n_list)
	draw_board(c_list)
	if is_winner(player_2, c_list):
		print("\nPlayer 2 WINS!!!!!!")
		break
	