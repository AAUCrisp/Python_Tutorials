#Ask the user for a string and print out whether this string is a
#  palindrome or not. (A palindrome is a string that reads the 
# same forwards and backwards.)

word = str(input("Enter a word to see if it´s a palindrome: "))

rvs = word[::-1]

if word == rvs:
    print("True,", word,"is a palindrome." )
else:
    print("False,", word, "isn´t a palindrome.")