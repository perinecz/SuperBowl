class Donto:
    def __init__(self, adatsor):
        reszletek = adatsor.split(";")
        #adatmezők kialakítása
        self.ssz = reszletek[0]
        self.datum = reszletek[1]
        self.gyoztes = reszletek[2]
        self.ererdmeny = reszletek[3]
        self.vesztes = reszletek[4]
        self.helyszin = reszletek[5]
        self.varosAllam = reszletek[6]
        self.nezoszam = int(reszletek[7])

    def __str__(self):
        return f"{self.datum}, {self.helyszin}: {self.gyoztes} - {self.vesztes} ({self.ererdmeny})"
    
    def pontKulonbseg(self):
        reszletek = self.ererdmeny.split('-')
        return int(reszletek[0]) - int(reszletek[1])
    

#0
print("Super Bowl döntőinek feldolgozása")

#1
finp = open("SuperBowl.txt", mode="rt", encoding="utf8")
adatsorok = finp.read().split('\n')
finp.close()

dontok = []
for i in range(1, len(adatsorok)):
    if adatsorok[i] != "":
        dd = Donto(adatsorok[i])
        dontok.append(dd)

for item in dontok:
    print(item)
print("------------------------------------------------")

#Programozási tételek
#Összegzés tétele
#
sum = 0
for item in dontok:
    sum += item.nezoszam
print(f"sum = {sum}")
print("------------------------------------------------")

#átlag
#
sum = 0
for item in dontok:
    sum += item.nezoszam
atlag = sum / len(dontok)
print(f"átlag = {atlag:.2f}")
print("------------------------------------------------")

#min - max tétel
#min
#
minPontkulonbseg = dontok[0]
for item in dontok:
    if item.pontKulonbseg() < minPontkulonbseg.pontKulonbseg():
        minPontkulonbseg = item
print(f"min pontkülönbség: {minPontkulonbseg.pontKulonbseg()}")
print("------------------------------------------------")

#max
#
maxPontkulonbseg = dontok[0]
for item in dontok:
    if item.pontKulonbseg() > maxPontkulonbseg.pontKulonbseg():
        maxPontkulonbseg = item
print(f"max pontkülönbség: {maxPontkulonbseg.pontKulonbseg()}")
print("------------------------------------------------")

#
maxNezoszam = dontok[0]
for item in dontok:
    if item.nezoszam > maxNezoszam.nezoszam:
        maxNezoszam = item
print(f"max nézőszám: {maxNezoszam.nezoszam}")
print("------------------------------------------------")

#megszámlálás tétele
#
dbPS = 0
for item in dontok:
    if item.gyoztes == "Pittsburgh Steelers":
        dbPS += 1

print(f"A 'Pittsburgh Steelers' csapat {dbPS} győzött a döntők során")
print("------------------------------------------------")


#eldöntés tétele
#legalabb egy elem teljesíti a feltételt
#
vanEpontKul50tobb = False
for item in dontok:
    if item.pontKulonbseg() > 50:
        vanEpontKul50tobb = True
        break
if vanEpontKul50tobb:
    print("Igen volt megfelelő döntő")
else:
    print("Nem volt megfelelő döntő")
print("------------------------------------------------")

#minden elem teljesíti
#
mindenEnezoszam70eTobb = True
for item in dontok:
    if not (item.nezoszam > 70000):
        mindenEnezoszam70eTobb = False
        break
if mindenEnezoszam70eTobb:
    print("Minden döntő teljesíti a feltételt")
else:
    print("Nem inden döntő teljesíti a feltételt")
print("------------------------------------------------")

#kiválasztás tétele
#!!!!!!!!!!!!!!!!
#
dontoNezoszam100Etobb = None
for item in dontok:
    if item.nezoszam > 100000:
        dontoNezoszam100Etobb = item
        break
if dontoNezoszam100Etobb != None:
    print(f"Van ilyen döntő, amely nézőszáma: {dontoNezoszam100Etobb.nezoszam}")
else:
    print("Nincs megfelelő dőntő")
print("------------------------------------------------")


#Keresés tétele
#!!!!!!!!!!
#
indexPonKul10 = None
for i in range(len(dontok)):
    if dontok[i].pontKulonbseg() == 10:
        indexPonKul10 = i
        break
if indexPonKul10 != None:
    print(f"Döntő: {dontok[indexPonKul10]}, NÉZŐSZÁM: {dontok[indexPonKul10].nezoszam}")
else:
    print("Nincs megfelelő döntő")
print("------------------------------------------------")


#buborékos rendezés
#
for i in range(len(dontok)-1, 0, -1):
    for j in range(i):
        if dontok[j].pontKulonbseg() < dontok[j+1].pontKulonbseg():
            dontok[j], dontok[j+1] = dontok[j+1], dontok[j]  

for item in dontok:
    print(item)




