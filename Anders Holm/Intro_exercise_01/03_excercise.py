#Create a program that reads three integers from the user and displays 
# them in sorted order (from smallest to largest). 

a = int(input('Enter your first number: '))
b = int(input('Enter your secound number: '))
c = int(input('Enter your third number: '))

number_list = [a, b, c]
print(number_list.sort())