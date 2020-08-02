#Basketball Roster Program

#Creating Empty List
roster=[]
print("Welcome to Basketball Player Roster Program \n")
#Adding the user via input to the list
roster.append(input("Enter Player One Detail : ").title())
roster.append(input("Enter Player Two Detail : ").title())
roster.append(input("Enter Player Three Detail : ").title())
roster.append(input("Enter Player Four Detail : ").title())
roster.append(input("Enter Player Five Detail : ").title())

#Display roster
print("\nThe Basketball Players for the upcoming season")
print("\n\t Point Guard : \t\t" + roster[0])
print("\t Forward Guard : \t" + roster[1])
print("\t Small Guard : \t\t" + roster[2])
print("\t Power Guard : \t\t" + roster[3])
print("\t Center : \t\t" + roster[4])

#Remove Injured player 
#Removing the player Three 
injured_player = roster.pop(2)
print(f"\nOh no, {injured_player} is injured.")

#length of the basketball players
roster_len=len(roster)
print(f"\nYou Roster has {roster_len} players")

#Add new player to the roster
roster_new=input("Enter the new player name : ").title()
roster.insert(2,roster_new)

#Final Players list
print("\nThe Basketball Players for the upcoming season")
print("\n\t Point Guard : \t\t" + roster[0])
print("\t Forward Guard : \t" + roster[1])
print("\t Small Guard : \t\t" + roster[2])
print("\t Power Guard : \t\t" + roster[3])
print("\t Center : \t\t" + roster[4])

print("\nGood Luck Team!!!")
roster_len=len(roster)
print(f"\nYou Roster has {roster_len} players")
