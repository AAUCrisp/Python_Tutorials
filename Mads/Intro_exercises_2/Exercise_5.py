import time

def velkomst():
    Navn = input('Hvad er dit navn? \n ')
    Alder = input('Hvad er din alder? \n ')
    Status = input('Hvad er din privatstatus \n ')
    print('Hej', Navn, 'Du er', Alder, 'og er', Status)



def loading():
    start = 1
    while(start==1): 
        print('.')
        time.sleep(1)


def Lorteprogram():
    velkomst()
    loading()


Lorteprogram()