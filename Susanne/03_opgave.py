#Promting the user to enter 3 integers
first = int(input("Enter first integer: "))
second = int(input("Enter second integer: "))
third = int(input("Enter third integer: "))

print("The 3 integers are...", first, second, third) 

#defining smallest, largest and middle integer
smallest = min(first, second, third)
largest = max(first, second, third)
middle = (first + second + third) - smallest - largest

#printing the result in sorted order
print("The integers in sorted order is:",smallest,",",middle,",",largest)