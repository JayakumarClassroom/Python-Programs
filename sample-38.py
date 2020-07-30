#Favorite Teachers list

print("Welcome to the Favorite Teachers Program\n")

#Creating Empty List
fav_teachers=[]
fav_teachers.append(input("Who is Your Favorite Teacher : ").title())
fav_teachers.append(input("Who is Your Favorite Teacher : ").title())
fav_teachers.append(input("Who is Your Favorite Teacher : ").title())
fav_teachers.append(input("Who is Your Favorite Teacher : ").title())

#Displaying the Favorite Teahcers Name list
print("\nYour Favorite Teachers are ", fav_teachers)

#Sorted Order 
print("Your favorite teachers in ascending order: ", sorted(fav_teachers))

#Reverse Order
print("Your favorite teachers in reverse order: ", sorted(fav_teachers, reverse=True))

#Top favorite teachers
print("\nYour top two favorite teachers are : " + str(fav_teachers[0])+" "+ str(fav_teachers[1]))
print("Your next two favorite teachers are : " + str(fav_teachers[2] )+" "+  str(fav_teachers[3]))
print("Your last favorite teacher is : " + str(fav_teachers[-1]))

#number of favorite teachers 
print("You have total of ", len(fav_teachers) ," favorite teachers.")


print(f"\nOops {fav_teachers[0]} is no longer your first favorite teacher.")

#adding new first favorite teacher
fav_teachers_new=input("Who is your new favorite teacher : ").title()
fav_teachers.insert(0,fav_teachers_new)

print("\nYour top two favorite teachers are : " + str(fav_teachers[0])+" "+ str(fav_teachers[1]))
print("Your next two favorite teachers are : " + str(fav_teachers[2] )+" "+  str(fav_teachers[3]))
print("Your last favorite teacher is : " + str(fav_teachers[-1]))


print("You have total of ", len(fav_teachers) ," favorite teachers.")


#Removing Favorite teacher

fav_teachers_remove=input("You decided you no longer like a teahcer. Which teacher you like to remove ? ").title()
fav_teachers.remove(fav_teachers_remove)



print("\nYour top two favorite teachers are : " + str(fav_teachers[0])+ " " + str(fav_teachers[1]))
print("Your next two favorite teachers are : " + str(fav_teachers[2] )+ " " +  str(fav_teachers[3]))
print("Your last favorite teacher is : " + str(fav_teachers[-1]))


print("You have total of ", len(fav_teachers) ," favorite teachers.")