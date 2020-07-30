#Functions - List - Local and Global Variables


def remove_name(names):
	#Remove the name from the friends list
	removed = names.pop()
	print(f"Good byeee {removed.upper()}.")
	print(f'After Removed: {names}')

friends=['Jay','Mike','sam','kumar']

print(f'Friends List : {friends}')

remove_name(friends)