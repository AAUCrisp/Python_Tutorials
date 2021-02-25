# ------ SUBMODULE 2 -----
# From Submodule 2 PDF on Moodle
#%% -- Opgave 1 --
#Write a program that asks the user to enter the width and length of a room. Once the values have been read, your program should compute and display the area of the room. The length and the width will be entered as floating point numbers. Include units in your prompt and output message either feet or meters, depending on which unit you are more comfortable working with.

width = float(input("Width of the house? "))
height = float(input("Length of the house? "))

print(width*height)

#%% -- Opgave 2 --
# Develop a program that begins by reading a number of seconds from the user. Then your program should display the equivalent amount of time in the form D: HH: MM: SS, where D, HH, MM, and SS represent days, hours, minutes and seconds respectively. The hours, minutes and seconds should all be formatted so that they occupy exactly two digits, with a leading 0 displayed if necessary

number = int(input("Input an amount of seconds, to convert to Days, Hours, Minutes and Seconds "))

# % dividere med tallet efter og gemmer RESTEN ... ikke det hele tal der kommer efter divisionen.
seconds = number % 60
minutes = number / 60 % 60
hours = number / 60 / 60 % 24
# days = number / 60 / 60 / 24 % 1     # HUH!?!?! Hvorfor bliver den en float når alle de andre virker som de skal
# days = int(number / 60 / 60 / 24) % 1   # Hvorfor?
days = int(number / 60 / 60 / 24)   # Virker..... nogle gange

print(number ," Seconds is ", days, ": %02d" % hours, ": %02d" % minutes, ": %02d" % seconds)
# print(number ," Seconds is ", days, ":" , hours , ":", minutes, ":", seconds)

# %% -- Opgave 3 --
# Create a program that reads three integers from the user and displays them in sorted order (from smallest to largest).

n1 = float(input("Write a number"))
n2 = float(input("Write another number"))
n3 = float(input("Write a third and last number"))

print("Your numbers are", n1, n2, n3)
minimum = min(n1, n2, n3)
maximum = max(n1, n2, n3)
middle = (n1 + n2 + n3) - (minimum + maximum)

print("In sorted order they're " , minimum, middle, maximum)

# %% Opgave 4 & 5
# Opgave 4: Write a function that takes three numbers as parameters and returns the median value of those parameters as its result. Include a main program that reads three values from the user and displays their median.
# Opgave 5: Write and test a Python program that access a function inside a function.


def findMedian(a, b, c):
    return (a + b + c) - min(a, b, c) - max(a, b, c)

def main():
    n1 = float(input("Write a number"))
    n2 = float(input("Write another number"))
    n3 = float(input("Write a third and last number"))

    print("Your numbers are", n1 , "," , n2 , "&" , n3 , "The median of those numbers are", findMedian(n1, n2, n3))

main()

# %% Opgave 6
# Write and test a Python program that access a function inside a function.

def listToList(a, b, pos):
    # Reverse the list, for easier access to the end-index
    a.reverse()
    # Add the "back" of a-list, to the desired positon in the b-list (not deleting any entries)
    b[pos:pos] = [a[0]]
    return b

numbers = [12, 32, 5, 4]
fuck = ["abe", "nisse", "fisk", "hamster"]

print(listToList(numbers, fuck, 2))


# %% Opgave 7
# Repeat the previous exercise with tuples.

def tupToTup(a, b, pos):
    #convert the Tuples to Lists
    aList = list(a)
    bList =list(b)

    # Reverse the list, for easier access to the end-index
    aList.reverse()
    # Add the "back" of a-list, to the desired positon in the b-list (not deleting any entries)
    bList[pos:pos] = [aList[0]]
    return tuple(bList)


numbers = (12, 32, 5, 4)
fuck = ("abe", "nisse", "fisk", "hamster")

print(tupToTup(numbers, fuck, 2))
