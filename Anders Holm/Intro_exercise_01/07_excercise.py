#Write a function that takes two lists and one integer as inputs and 
# moves the last element of the first list to the second list at the 
# specific position defined by the integer.

#Repeat the previous exercise with tuples.

a_tuple = (1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89)
b_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)

position = int(input('What position should the number be moved to: '))

#convert a and b tuple to lists
a_list = list(a_tuple)
b_list = list(b_tuple)

#removes the last number in a
d = a_list[-1]
a_list.remove(d)

#insert the last number from a in b
b_list.insert(position, d)

#convert a and b list back to tuple
a_tuple = tuple(a_list)
b_tuple = tuple(b_list)

#confirm operation
print(type(b_tuple))
print(b_tuple)


