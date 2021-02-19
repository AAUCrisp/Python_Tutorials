#Ask the user for a number. Depending on whether the number is even or odd,
# print out an appropriate message to the user.

number = input("Enter a random number: ")

#makes the str variable number into a int 
number = int(number)

if number%2 == 0:
    print("Your number is even")
else:
    print("Your number is odd")