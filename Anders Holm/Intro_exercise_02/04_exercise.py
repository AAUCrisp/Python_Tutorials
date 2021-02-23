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

def enterBit(): 
    a = input('Enter seven random bits: ')
    return a

userBit = enterBit()
if userBit.isnumeric() == True:
    if len(userBit) > 7:
        print('ERROR - you entered to much')
        enterBit()
    elif len(userBit) == 7:
        count = userBit.count("0")
        if count%2 == 0:
            print('The parity bit should be 1')
        else:
            print('The parity bit should be 0')
    elif len(userBit) < 7:
        print('ERROR - you didnt type enough')
        enterBit()
else:
    print('Error - try again')
    print('Remember to only use bits')
    enterBit()