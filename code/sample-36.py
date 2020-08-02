#Grocery List APP 
#Adding,sorting, removing the items to the list


import datetime

print("welcome to Grocery App List \n")
#date and time 
a=datetime.datetime.now()
mon=str(a.month)
da=str(a.day)
hou=str(a.hour)
mini=str(a.minute)
sec=str(a.second)
print(f"Current Date and Time is {mon}/{da} {hou}:{mini}:{sec}")

# default items in the grocery list

list_groc=["Cheese","Apple"]
print('Items in your Grocery List are : '+ str(list_groc),"\n")

#adding the items to existing grocery list
list_groc.append(input("Enter the Items to Add to your List : ").title())
list_groc.append(input("Enter the Items to Add to your List : ").title())
list_groc.append(input("Enter the Items to Add to your List : ").title())

#printing the items
print("\n Items in your Grocery App List \n" + str(list_groc))

#printing the items in ascending order
print("\nSorted Items in your Grocery List \n",sorted(list_groc))

#Removing the purchased items 
a=input("\nEnter the purchased item : ").title()
list_groc.remove(a)
print("\n",len(list_groc) ," items in your Grocery List \n", sorted(list_groc))

a=input("\nEnter the purchased item : ").title()
list_groc.remove(a)
print("\n",len(list_groc) ," items in your Grocery List \n", sorted(list_groc))

a=input("\nEnter the purchased item : ").title()
list_groc.remove(a)
print("\n",len(list_groc) ," items in your Grocery List \n", sorted(list_groc))

#out of stock items
no_item=list_groc.pop()
print(f"\n The {no_item} items your expecting is not available")

#new item to the grocery list
new_food = input("Enter the item to added instead of : ").title()
list_groc.append(new_food)

#final items in your list
print("\n Items in your grocery list", list_groc)