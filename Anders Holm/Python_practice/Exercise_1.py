#Create a program that asks the user to enter their name and their age. 
#Print out a message addressed to them that tells them the year 
# that they will turn 100 years old.


name = input("What is your first name: ")
age = input("How old are you: ")

old_age = int(age) + 100

print("Your name is",name, "and in a 100 years you will be",old_age,"years old.")