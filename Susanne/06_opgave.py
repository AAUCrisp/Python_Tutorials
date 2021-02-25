#Write  a  function  that  takes  two  lists  and  one  integer  as  inputs  and  moves  the  last  element  of  the  first list to the second list at the specific position defined by the integer

#defining a function that prompts the user to enter a integer to be moved:
def PositionMove(list1, list2):
    move = int(input("Enter the number you want the last element of first list to be moved to in the second list:"))
    lastNumber = list1[-1]
    list1.remove(lastNumber)
    list2.insert(move, lastNumber)

#defining a function that defines the lists and calls the above function
def main():
    list1 = [1,2,3,4,5,6,7,8,9,10]
    list2 = [10,9,8,7,6,5,4,3,2,1]
    PositionMove(list1, list2)
    print("The new list is", list2)

#calling the main function
main()
