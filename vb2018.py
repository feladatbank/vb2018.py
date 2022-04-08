'''
varos;nev1;nev2;ferohely
Moszkva;Luzsnyiki Stadion;n.a.;78011
Moszkva;Otkrityije Aréna;Szpartak Stadion;44190
'''
class Vilagbajnoksag:
    def __init__(self,sor):
        varos, nev1, nev2, ferohely = sor.strip().split(";")
        self.varos = varos
        self.nev1 = nev1
        self.nev2 = nev2
        self.ferohely = ferohely
    


lista=[]
with open("vb2018.txt", encoding="latin2") as f:
    f.readline()
    for sor in f:
        lista.append(Vilagbajnoksag(sor))

#3 feladat

stadionok=[]    
for sor in lista:
    stadionok.append(sor.nev1)
print(f"Stadionok száma:{len(stadionok)}")
    
#4 feladat    
stadion=""
varos=""
ferohely=lista[0].ferohely

for sor in lista:
    if sor.ferohely < ferohely:
        ferohely = sor.ferohely
        stadion = sor.nev1
        varos = sor.varos
print(f"""Legkevesebb férőhely:
    Város: {varos}
    Stadium: {stadion}
    Férőhely: {ferohely}""")

#5 feladat
ferohelyek=[]
for sor in lista:
    ferohelyek.append(int(sor.ferohely))
    
ossz = sum(ferohelyek)
atlag = ossz / len(ferohelyek)
atlag = f"{atlag:.1f}"
atlag = str(atlag)
atlag = atlag.replace(".",",")
print(f"Átlag férőhely szám:{atlag}")
    
#6 feladat
'''
szamlalo = 0 
for sor in lista:
    if sor.nev2 == "n.a.":
        szamlalo += 1
print(f"Stadionok kettő névvel:{len(stadionok)-szamlalo}")
'''    
szamlalo = 0
for sor in lista:  
    if sor.nev2 != "n.a.":
        pass
    else:
        szamlalo += 1
print(f"Stadionok kettő névvel:{szamlalo}")


















#7    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    