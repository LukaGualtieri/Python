#1
import pprint
pp=pprint.PrettyPrinter(indent=4)
tabella={"Giuseppe Gullo":[("Corsa Campestre",(40,21,0),"Allievi"),("Corsa 100mt",(0,12,0),"Juniores mas"),("Corsa 200mt",(0,29,19),"Juniores mas")],
         "Antonia Barbera":[("Corsa Campestre",(0,39,11),"Juniores fem"),("Corsa 100mt",(0,18,0),"Juniores fem"),("Corsa 200mt",(0,0,0),"Juniores fem")],
         "Nicola Esposito":[("Corsa Campestre",(0,43,22),"Allievi"),("Corsa 100mt",(0,14,0),"Juniores mas"),("Corsa 200mt",(0,36,19),"Juniores mas")]}
pp.pprint(tabella)


#2
import pprint
pp=pprint.PrettyPrinter(indent=4)
tabella["Luka Gualtieri"]=[("Corsa Campestre",(50,21,0),"Allievi"),("Corsa 100mt",(0,10,0),"Juniores mas"),("Corsa 200mt",(0,24,10),"Juniores mas")]
pp.pprint(tabella)


#3   Finito alle 9.30 (Prof Spinarelli)
import pprint
pp=pprint.PrettyPrinter(indent=4)

newDisciplina=tabella["Giuseppe Gullo"]
newDisciplina.append(("Corsa ad ostacoli 400mt",(0,40,34),"Allievo"))
tabella["Giuseppe Gullo"]=newDisciplina

newDisciplina=tabella["Antonia Barbera"]
newDisciplina.append(("Corsa ad ostacoli 400mt",(0,39,10),"Allieva"))
tabella["Antonia Barbera"]=newDisciplina

newDisciplina=tabella["Nicola Esposito"]
newDisciplina.append(("Corsa ad ostacoli 400mt",(0,40,10),"Allievo"))
tabella["Nicola Esposito"]=newDisciplina

newDisciplina=tabella["Luka Gualtieri"]
newDisciplina.append(("Corsa ad ostacoli 400mt",(0,40,26),"Allievo"))
tabella["Luka Gualtieri"]=newDisciplina

pp.pprint(tabella)


#4  Finito alle 9.33 (Prof Spinarelli)
print("Le informazioni sulla disciplina sportiva Corsa Campestre per Giusepppe Gullo: ")
print(f"Disciplina: {(tabella['Giuseppe Gullo'][0][0])}")
print(f"Tempo in min,sec,cent: {(tabella['Giuseppe Gullo'][0][1])}")
print(f"Categoria: {(tabella['Giuseppe Gullo'][0][2])}")


#5  Finito alle 9.45 (Prof Spinarelli)
print("Il tempo per la corsa 200mt di Nicola Esposito è: ")
print(f"Minuti: {(tabella['Nicola Esposito'][2][1][0])}")
print(f"Secondi: {(tabella['Nicola Esposito'][2][1][1])}")
print(f"Centesimi: {(tabella['Nicola Esposito'][2][1][2])}")


 #6 Finito alle 9.48 (Prof Spinarelli)
print("Il tempo per la corsa 100mt di Antonia Barbera è: ")
print(f"Minuti: {(tabella['Antonia Barbera'][1][1][0])}")
print(f"Secondi: {(tabella['Antonia Barbera'][1][1][1])}")
print(f"Centesimi: {(tabella['Antonia Barbera'][1][1][2])}")


#7 Finito alle 10.20 (Prof Spinarelli)
print("Il tempo minimo riportato nella corsa 100mt della categoria Juniores mas è: ")
min=0

t1=tabella["Giuseppe Gullo"][1][1]
t2=tabella["Luka Gualtieri"][1][1]
t3=tabella["Nicola Esposito"][1][1]

for i in range(len(tabella)):
  if (t1<t2):
    min=t1
  elif (t2<t3):
    min=t2
  else:
    min=t3

print(min)


#8  Finito alle 10.29 (Prof Spinarelli)
print("Il tempo massimo riportato nella corsa 200mt della categoria Juniores mas è: ")
max=0
te1=tabella["Giuseppe Gullo"][2][1]
te2=tabella["Luka Gualtieri"][2][1]
te3=tabella["Nicola Esposito"][2][1]

for i in range(len(tabella)):
  if (te1>te2):
    max=te1
    if (te2>te3):
      max=te2
    else:
      max=te3
  
print(max)


#9  Finito alle 10.48 (Prof Spinarelli)
print("La media dei tempi della categoria Allievi nella Corsa Campestre è: ")
mMin=0
mSec=0
mCent=0

min1=tabella["Giuseppe Gullo"][0][1][0]
min2=tabella["Luka Gualtieri"][1][1][0]
min3=tabella["Nicola Esposito"][2][1][0]

sec1=tabella["Giuseppe Gullo"][0][1][1]
sec2=tabella["Luka Gualtieri"][1][1][1]
sec3=tabella["Nicola Esposito"][2][1][1]

cent1=tabella["Giuseppe Gullo"][0][1][2]
cent2=tabella["Luka Gualtieri"][1][1][2]
cent3=tabella["Nicola Esposito"][2][1][2]

mMin=min1+min2+min3/len(tabella)
mSec=sec1+sec2+sec3/len(tabella)
mCent=cent1+cent2+cent3/len(tabella)

print(f"Media dei minuti: {mMin:.0f}")
print(f"Media dei secondi: {mSec:.0f}")
print(f"media dei centesimi: {mCent:.0f}")
print(f"Tempo Medio: {mMin:.0f}.{mSec:.0f}.{mCent:.0f}")
