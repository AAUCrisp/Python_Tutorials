#Create a program that reads the name of a month from the user as a 
# string and then displays the number of days in that month. 
# The length of a month varies from 28 to 31 days.

month_list = ['januar','februar','marts','april','maj','juni','juli','august','september','oktober','november','december']
days_month = ['31','28','31','30','31','30','31','31','30','31','30','31']

#user types a month
month = input('Enter a month to know the number of days: ')

#all letters are set to lowercases
month = month.casefold()

#finds the index number in month list
number = int(month_list.index(month))

#finds the matching number of days to that month
month = month.capitalize()
days = days_month[number]

print(month,'has',days,'days')
