#here we will write an extremely simple programme that accesses a function within a function

#defining function that adds numbers a and b
def AddNumbers(a,b):
    return(a + b)

#defining function that defines the numbers a and b, calls the above function and print the answer
def main():
    a = 25
    b = 55
    AddNumbers(a,b)
    print("The numbers added together is:", AddNumbers(a,b))

#calling the main function
main()
