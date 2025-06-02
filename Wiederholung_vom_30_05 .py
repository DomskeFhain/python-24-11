###### Abschnitt 3.1 - Listen
# # christofs_liste = ["Python","C++","Java","C#","Javascript"]

# print(christofs_liste[0]) # indexierung
# print(christofs_liste[:3]) # slicing startwert:endwert:sprungwert
# print(christofs_liste[-1]) # Javascript
# print(christofs_liste[::-1]) # reversed die Liste

# christofs_liste.append("Swift")
# print(christofs_liste)

# christofs_liste.insert(2,"C")
# print(christofs_liste)

# print(christofs_liste.index("Java"))

# print(sorted(christofs_liste)) ## Die originale Liste wird nicht verändert
# print(christofs_liste)

# christofs_liste.sort() # die originale lsite wird verändert
# print(christofs_liste)

# del christofs_liste[0:3]
# print(christofs_liste)

# christofs_liste.remove("Swift")
# print(christofs_liste)

# print(christofs_liste.pop(0)) 


# farben = ["rot","grün","blau","gelb","violett","dunkelrot"]
# for farbe in farben:
#     print(f"Deine Tolle Farbe ist: {farbe}")

# print("rot" in farben)
# print("rosa" not in farben)

# quadrate = []
# for i in range(10):
#     quadrate.append(i**2) 

# print(quadrate)

# quadrate = [i**2 for i in range(10)]
# print(quadrate)

# zahl1 = 100
# zahl2 = zahl1

# zahl1 = 200

# print(zahl1)
# print(zahl2)

# zahlen1 = [1,2,3]
# # zahlen2 = zahlen1
# # zahlen2 = zahlen1.copy()
# # zahlen2 = list(zahlen1)
# zahlen2 = zahlen1[:]
# zahlen1.append(4)


# print(zahlen1)
# print(zahlen2)

# matrix = [["-","-","-"],["-","-","-"],["-","-","-"]]
# matrix2 = [["1","2","3"],["4","5","6"],["7","8","9"]]
# print("Die länge der Liste beträgt:" + str(len(matrix)))
# print(matrix2[1][1]) # 5

# print(len(matrix[0]))

# for zeile in matrix:
#     print(zeile)

######### Abschnitt 3.2 - Tuples

# farben = ("rot","grün","blau","gelb","violett","dunkelrot")
# print(farben[0:4])

# for farbe in farben:
#     print(farbe)

# daten = [("Joshua",31,"Köln"),("Suheib",28,"Frankfurt")] 
# daten.append(("Katharina",30,"Berlin"))

# daten2 = (["Joshua",31,"Köln"],["Suheib",28,"Frankfurt"])
# # daten2.append(("Katharina",30,"Berlin")) ## das funktioniert nicht bei einem tuple
# daten2[0][1] = 29
# print(daten2)





