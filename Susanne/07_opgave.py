#Repeat the previous exercise with tuples

#defining the tuples
tuple1 = (1,2,3,4,5,6,7,8,9,10)
tuple2 = (10,9,8,7,6,5,4,3,2,1)  

#converting the tuples to lists
list1 = list(tuple1)
list2 = list(tuple2)

#defining a function that removes last number from list 1 to user input in list 2
#converts the lists back to tuples 
def main():
    move = int(input("Enter the position you want the last element of first list to be moved to in the second list:"))
    lastNumber = list1[-1]
    list1.remove(lastNumber)
    list2.insert(move, lastNumber)
    tuple1 = tuple(list1)
    tuple2 = tuple(list2)
    print("The new list is as follows:",tuple2)

#calling the main function
main()

