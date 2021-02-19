#Develop a program that begins by reading a number of seconds from the user. 
# Then your program should display the equivalent amount of time in the 
# form D:HH:MM:SS, where D, HH, MM, and SS represent days, hours, minutes 
# and seconds respectively. The hours, minutes and seconds should all be 
# formatted so that they occupy exactly two digits, with a leading 0 displayed 
# if necessary.

SECONDS_PER_MINUTE  = 60
SECONDS_PER_HOUR    = 3600
SECONDS_PER_DAY     = 86400
 
seconds = int(input("Enter a random number of seconds: "))
 
#Calculate the days, hours, minutes and seconds
days = seconds / SECONDS_PER_DAY
seconds = seconds % SECONDS_PER_DAY
 
hours = seconds / SECONDS_PER_HOUR
seconds = seconds % SECONDS_PER_HOUR
 
minutes = seconds / SECONDS_PER_MINUTE
seconds = seconds % SECONDS_PER_MINUTE
 
#Display the result
print("The duration is: ","%0d:%02d:%02d:%02d"%(days,hours,minutes,seconds))