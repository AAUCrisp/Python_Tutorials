#Create a program that asks the user for a number and then prints 
# out a list of all the divisors of that number. (If you don’t 
# know what a divisor is, it is a number that divides evenly into 
# another number. For example, 13 is a divisor of 26 because 26 / 13 
# has no remainder.)

number = int(input("Enter a random number between 0 and 100: "))

test_list = range(2, number)
even_list = []

for x in test_list:
    if number%x == 0:
        even_list.append(x)
print(even_list)
