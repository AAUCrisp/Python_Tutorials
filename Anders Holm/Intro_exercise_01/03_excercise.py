#Create a program that reads three integers from the user and displays 
# them in sorted order (from smallest to largest). 

number_one = int(input('Enter your first number: '))
number_two = int(input('Enter your secound number: '))
number_three = int(input('Enter your third number: '))

number_list = [number_one, number_two, number_three]
number_list.sort()

print(number_list)