'''
Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:
	Rock beats scissors 
	Scissors beats paper
	Paper beats rock
'''

a = input("player A: ")
b = input("player B: ")
win = {"P":"R","R":"S","S":"P"}
if a == b:
	print("No winner")
else:
	print("Winner is player " + "A" if win[a] == b else "B")