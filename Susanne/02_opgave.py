#here we will write a programme that displays a number of seconds in the terms of years, days, minutes and seconds.

#prompting the user to write a number of seconds in the terminal
AnyNumber = float(input("Enter any number of seconds: ")) 

print("The number of seconds entered is:", AnyNumber)
print("Which in days, hours, minutes and seconds is the following:")

#dividing into minutes, hours & days
seconds = int(AnyNumber % 60)         
minutes = int((AnyNumber / 60) % 60)    
hours = int((AnyNumber / 60 / 60) % 24) 
days = int((AnyNumber / 60 / 60 / 24)) 

#printing the result
print(days,':',"%02d"%hours,':',"%02d"%minutes,':',seconds) 