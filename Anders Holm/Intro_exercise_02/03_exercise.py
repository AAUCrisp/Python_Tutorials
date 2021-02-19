#A particular zoo determines the price of admission based on the age of the guest. 
# Guests 2 years of age and less are admitted without charge. Children between 3 
# and 12 years of age cost 20.00 kr. Seniors aged 65 years and over cost 25.00 kr. 
# Admission for all other guests is 50.00 kr.

#Create a program that begins by reading the ages of all of the guests in a group 
# from the user, with one age entered on each line. The user will enter a blank 
# line to indicate that there are no more guests in the group. Then your program 
# should display the admission cost for the group with an appropriate message.

import random

#price for different groups
kids_price = 0.00
children_price = 20.00
adult_price = 50.00
senior_price = 25.00

#generate a random group of people with random ages
group_list = []
i = 0
group = random.randint(2,10)
while i < group: 
    random_number = random.randint(0,99)
    group_list.append(random_number)
    i += 1

#count number of people in different age group
kids = 0
children = 0 
adult = 0
senior = 0
for x in group_list:
    if x <= 2:
        kids += 1
    elif x > 3 and x < 13:
        children += 1
    elif x > 65:
        senior += 1
    else:
        adult += 1

#calculate the price for every age group and total price
a_kids = kids * kids_price
a_children = children * children_price
a_adult = adult * adult_price
a_senior = senior * senior_price

total_price = a_kids + a_children + a_adult + a_senior
tax = total_price * 0.2

#prints the bill for the entire group
print('Welcome to Aalborg Zoo')
print(' ')
print('Number of people in your group:')
print('Kids *', kids, '=',a_kids)
print('Children *', children, '=',a_children)
print('Adult *', adult, '=',a_adult)
print('Senior *', senior, '=',a_senior)
print(' ')
print('Total price:',total_price)
print('Taxes constitutes:',tax)
print(' ')
print('Have a pleasent day')


#print(group_list)
#print(kids)
#print(children)
#print(adult)
#print(senior)