st = input("write any number and i will tell you if it is even or not:   ")
i = int(st)
def OddEven():
    # denne funktion tager tallet der er givet, dividere det med 2, og derefter ser om der er noget i overskud.
    # hvis tallet ikke går op i to, så er der overskud, i form af decimaler.
    # derved er tallet ulige.
    # vice versa.
    n = i % 2
    if (n < 1):
        print("%d er lige" % i )
    else:
        print("%d er ulige" % i)


OddEven()
