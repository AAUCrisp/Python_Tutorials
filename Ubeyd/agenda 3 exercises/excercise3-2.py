Months = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november",
          "december"]
DN = ['31', '28', '31', '30', '31', '30', '31', '31', '30', '31', '30', '31']

# beder om input fra brugeren
st = input("what Month are we in?:  ")

# sørger for at input står i lower-case
st.lower()


def returnN():
    # index returnere index-værdien af string-indholdet.
    # string-indholdet er måneden. det man får retur, er et tal
    Months.index(st)
    # her printes værdien i DN listen, som ligger på tilsvarende index som Months listen.
    print(DN[Months.index(st)])



returnN()



"""
if st == Months[0]:
    print("there are 31 days in " + Months[0])
elif st == Months[1]:
    print("there are 28 days in " + Months[1])
elif st == Months[2]:
    print("there are 31 days in " + Months[2])
elif st == Months[3]:
    print("there are 30 days in " + Months[3])
elif st == Months[4]:
    print("there are 31 days in " + Months[4])
elif st == Months[5]:
    print("there are 30 days in " + Months[5])
elif st == Months[6]:
    print("there are 31 days in " + Months[6])
elif st == Months[7]:
    print("there are 31 days in " + Months[7])
elif st == Months[8]:
    print("there are 30 days in " + Months[8])
elif st == Months[9]:
    print("there are 31 days in " + Months[9])
elif st == Months[10]:
    print("there are 30 days in " + Months[10])
elif st == Months[11]:
    print("there are 31 days in " + Months[11])
"""
