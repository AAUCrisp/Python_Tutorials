#A parity bit is a simple mechanism for detecting errors in data transmitted over an unreliable
#connection such as a telephone line. The basic idea is that an additional bit is transmitted after each
#byte (group of 8 bits) so that a single bit error in the transmission can be detected. Parity bits can be
#computed for either even parity or odd parity. If even parity is selected then the parity bit that is
#transmitted is chosen so that the total number of one bits transmitted (8 bits of data plus the parity
#bit) is even. When odd parity is selected the parity bit is chosen so that the total number of one bits
#transmitted is odd.

#Write a program that computes the parity bit for groups of 8 bits entered by the user using even
#parity. Your program should read strings containing 8 bits until the user enters a blank line. After
#each string is entered by the user your program should display a clear message indicating whether
#the parity bit should be 0 or 1. Display an appropriate error message if the user enters something
#other than 8 bits.

def getInput():
    while True:
        stringInput = input("Enter 8-bit string in binary: ")

        if len(stringInput) == 8:
            if (stringInput.count("1") + stringInput.count("0")) != 8:
                print("String does not consistent of 0 and 1")
            else:
                return stringInput
        else:
            print("Length of the string was not 8 bits. Try again.")

def checkBits(stringInput):
    if stringInput.count("1") % 2 == 0:
        print("parity bit should be 0")
    else:
        print("Parity bit should be 1")

def main():
    checkBits(getInput())

main()