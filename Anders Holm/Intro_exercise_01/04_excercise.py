#Write a function that takes three numbers as parameters and returns the 
# median value of those parameters as its result. Include a main program 
# that reads three values from the user and displays their median.

def f_median(a,b,c):
    d = (a+b+c) - min(a,b,c) - max(a,b,c)
    return d

def main():
    a = int(input('Enter your first number: '))
    b = int(input('Enter your second number: '))
    c = int(input('Enter your third number: '))

    print('The median number is',f_median(a,b,c))

main()