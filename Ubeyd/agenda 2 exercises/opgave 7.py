t = (1, 2, 3, 4, 5, 6)
u = (50, 51, 52, 53, 54, 55)

print(u)

L1 = list(t)
L2 = list(u)
x = L2[-1]


def opgave7(L1, L2, x):
    L2.insert(x, L1[-1])
    t = tuple(L1)
    u = tuple(L2)
    print(u)



opgave7(L1,L2,x)




