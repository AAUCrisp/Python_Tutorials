list1 = ["John", "Jenny", "Barbara"]
list2 = ["Green", "Red", "Blue"]


Length = len(list1)-1
Length2 = len(list2)-1

tal = int(input('Indsæt tal mellem 0 og {} \n'.format(Length2)))

def badfunction():
    list1[Length] = list2[tal]
    print(list1)


badfunction()