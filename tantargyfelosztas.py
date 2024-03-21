fajl = open('beosztas.txt')
forras = fajl.read().splitlines()
fajl.close()
adatok = [forras[i1:i1+4] for i1 in range(0,len(forras),4)] # [név,tantárgy,osztály,óraszám]
print('Bejegyzések száma:',len(adatok))
orak = [int(adat[3]) for adat in adatok]
print('Összesen',sum(orak),'óra van.')
tanarok = set([adat[0] for adat in adatok])
print(len(tanarok),'tanár tanít az iskolában.')

