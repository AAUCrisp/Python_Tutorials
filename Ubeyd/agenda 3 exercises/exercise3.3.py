group = input("how old are you").split()

adultprize = 0
childrenprize = 0
OGsprize = 0

adult = [elem * 1 for elem in group if 12 < int(elem) < 65]
children = [elem * 1 for elem in group if 2 < int(elem) < 13]
infant = [elem * 1 for elem in group if int(elem) < 2]
OGs = [elem * 1 for elem in group if int(elem) > 64]

for x in adult:
    adultprize += 50
for x in children:
    childrenprize += 20
for x in OGs:
    OGsprize += 25

prize = adultprize + childrenprize + OGsprize

print(prize)
