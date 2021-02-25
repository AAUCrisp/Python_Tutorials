tuple1 = ("John", "Jenny", "Barbara")
tuple2 = ("Green", "Red", "Blue")


Length = len(tuple1)-1
Length2 = len(tuple2)-1

list1 = list(tuple1)
list2 = list(tuple2)

tal = int(input('Indsæt tal mellem 0 og {} \n'.format(Length2)))

def badfunction():
    list1[Length] = list2[tal]
    tuple1 = tuple(list1)
    tuple2 = tuple(list2)
    print(tuple1)


badfunction()