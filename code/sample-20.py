#Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list. For practice, write this code inside a function.
'''
def listfunc(list_word):
	list_up=[]
	for x in list_word:
		list_up.append(list_word[0])
		list_up.append(list_word[-1])
		break

	print(list_up)
			
listfunc([1,2,3,4,5,6,7,8,9])
'''

def list_ends(a_list):
	print([a_list[0], a_list[-1]])

list_ends([1,2,3,4,5,6,7])