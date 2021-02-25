#here we will write a programme, that displays the area of a room from the users input of width and length.

width = float(input("Enter width in meters: ")) #this will prompt the user to write the width of the room in meters
length = float(input("Enter length in meters: ")) #this will prompt the user to write the length of the room in meters

print("Width in meters is: " , width) #The width is displayed in the terminal
print("Length in meters is " , length ) #The length is displayed in the terminal

areaRoom = width*length #width times length gives the area of the room

print("The area of the room in square meters is: " , areaRoom) #printing the area in terminal