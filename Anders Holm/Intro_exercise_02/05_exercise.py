#A string is a palindrome if it is identical forward and backward. For 
# example “anna”, “civic”, “level” and “hannah” are all examples of 
# palindromic words. Write a program that reads a string from the user
#  and uses a loop to determines whether or not it is a palindrome. 
# Display the result, including a meaningful output message.

word = str(input("Enter a word to see if it´s a palindrome: "))

rvs = word[::-1]

if word == rvs:
    print("True,", word,"is a palindrome." )
else:
    print("False,", word, "isn´t a palindrome.")