Regndetdogselv = float(input('Indtast antal sekunder der skal omregnes \n'))

S = int(Regndetdogselv % 60)

M = int((Regndetdogselv / 60) % 60)

H = int((Regndetdogselv / 60 / 60) % 24) 

D = int((Regndetdogselv / 60 / 60 / 24))

print(D,':',"%02d" % H,':',"%02d" % M,':',"%02d" % S)

