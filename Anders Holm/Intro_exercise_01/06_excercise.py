#Write a function that takes two lists and one integer as inputs and moves 
# the last element of the first list to the second list at the specific 
# position defined by the integer.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

position = int(input('What position should the number be moved to: '))

#removing last number in the list of a
c = a[-1]
a.remove(c)

#inserting the last number from a in b
b.insert(position, c)

print(b)