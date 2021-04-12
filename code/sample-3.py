#write a program that prints out all the elements of the list that are less than 5.

'''
Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
Write this in one line of Python.
Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.
'''

get_N_Input = int(input("Get N"))
list_word=[]
new_list=[]
for list_value in range(1,get_N_Input+1):
	list_word.append(int(input("Enter the valuesss")))

for new_list_value in list_word:
	if new_list_value < get_N_Input: #changed according to the N input numbers
		new_list.append(new_list_value)

print(sorted(new_list))