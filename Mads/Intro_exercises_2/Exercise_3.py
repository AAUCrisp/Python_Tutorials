Tal1=float(input('Indtast første tal: '))
Tal2=float(input('Indtast andet tal: '))
Tal3=float(input('Indtast tredje tal: '))

Mindste = min(Tal1, Tal2, Tal3)
Største = max(Tal1, Tal2, Tal3)
Midterste = (Tal1 + Tal2 + Tal3) - Mindste - Største

print(Mindste, Midterste, Største)
