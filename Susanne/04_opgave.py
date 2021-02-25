#in this programme we will find the median of 3 numbers entered by the user

#defining the function that will find the median (middle value)
def findMedian(a, b, c): 
    return (a + b + c) - min(a, b, c) - max(a, b, c)

#defining the function that will prompt the user to enter integers & call above function
def main():
    a = int(input("Enter first integer: ")) 
    b = int(input("Enter second integer: ")) 
    c = int(input("Enter third integer: ")) 
    findMedian(a,b,c)                     
    print("Medianen er...", findMedian(a,b,c))

#calling the main function to run the programme
main() 
