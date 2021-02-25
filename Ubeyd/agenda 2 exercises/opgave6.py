list1 = [1, 2, 3, 4, 5]
list2 = [420, 500, 590, 690, 700]


def opgave6(list1, list2, x):
    list2.insert(x, list1[4])    # indsætter en værdi på den ønskede plads i list2
    print(list2)


opgave6(list1, list2, 0)
