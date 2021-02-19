#Take a list, say for example this one:

#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#and write a program that prints out all the elements of the list that 
#are less than 5.

#Extras:
#1. Instead of printing the elements one by one, make a new list that has all
#  the elements less than 5 from this list in it and print out this new list.
#2. Write this in one line of Python.
#3. Ask the user for a number and return a list that contains only elements 
# from the original list a that are smaller than that number given by the user.

#Original assignment
prefix_list = [1, 1, 2, 3, 75, 5, 8, 13, 44, 21, 34, 65, 55, 89, 99]

for x in prefix_list:
    if x < 5:
        print(x)
    else:  #slows how many numbers are above 5
        print("-")
print(" ") #make space in terminal

#Extras:

#1. Instead of printing the elements one by one, make a new list that has all
#  the elements less than 5 from this list in it and print out this new list.
prefix_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
new_list = []

for x in prefix_list:
    if x < 5:
        new_list.append(x)
print(new_list)
print(" ")

#3. Ask the user for a number and return a list that contains only elements 
# from the original list a that are smaller than that number given by the user.
prefix_list = [1, 1, 2, 3, 75, 5, 8, 13, 44, 21, 34, 65, 55, 89, 99]
number = int(input("Enter a number between 0 and 100: "))

below_number = []

for x in prefix_list:
    if x < number:
        below_number.append(x)
print(below_number)