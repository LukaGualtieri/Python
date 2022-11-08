#1
import pprint
pp=pprint.PrettyPrinter(indent=4)
tabellaDati={"AA123BB":[("Giugno",9,1293),("Luglio",7,3231),("Agosto",7,4020),("Settembre",6,3928)],
             "AB345CD":[("Giugno",8,1391),("Luglio",6,1234),("Agosto",9,4932),("Settembre",8,2872)],
             "CD456FF":[("Giugno",7,2872),("Luglio",6,3273),("Agosto",4,3211),("Settembre",8,2827)]}
pp=pprint.PrettyPrinter(indent=4)

#2
import pprint
pp=pprint.PrettyPrinter(indent=4)
tabellaDati["ZZ999LG"]=[("Giugno",10,12000),("Luglio",10,12000),("Agosto",10,12000),("Settembre",10,12000)]
pp.pprint(tabellaDati)

#3
print(f"Mese: {(tabellaDati['AA123BB'][1][0])}")
print(f"Noleggi: {(tabellaDati['AA123BB'][1][1])}")
print(f"Kilometri: {(tabellaDati['AA123BB'][1][2])}")

#4
print(f"Noleggi nel mese di Luglio per la targa AA123BB: {(tabellaDati['AA123BB'][1][1])}")

#5
lista=tabellaDati["AA123BB"]
somma=0
for tupla in lista:
  #print(tupla[1])
  somma+=tupla[1]
print("La somma dei kilometri della targa AB345CD è:",somma)

#6
cont=0
for chiave in tabellaDati.keys():
  for i in range(len(tabellaDati[chiave])):
    cont+=tabellaDati[chiave][i][2]
print("La somma dei kilometri di tutte le auto è:",cont)

#7
max=0
mese=""
for i in range(len(tabellaDati["CD456FF"])):
  if tabellaDati["CD456FF"][i][2]>max:
    max=tabellaDati["CD456FF"][i][2]
    mese=tabellaDati["CD456FF"][i][0]
print("Il mese che cui si sono fatti più kilometri è:",mese)
print("I kilometri massimi sono: ",max)
