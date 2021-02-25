
def median(a,b,c):
    d = (a+b+c)-min(a,b,c)-max(a,b,c)
    print(d)



def main():
    a=float(input('indtast første tal: '))
    b=float(input('indtast andet tal: '))
    c=float(input('indtast tredje tal: '))
    median(a,b,c)
    
main()