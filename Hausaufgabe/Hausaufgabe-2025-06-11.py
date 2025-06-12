# def frage1():
#     print("""Hallo User, schaffst du es meine Fragen zu beantworten?
#           Welche dieser Variablennamen ist in Python nicht erlaubt?

#           A) my_var
#           B) _var 
#           C) 2var 
#           D) var_2
#     """)

#     antwort = input("Antwort: ")
#     if antwort == "C":
#         print("Richtig, Variablennamen dürfen nicht mit einer Ziffer beginnen")
#     elif antwort == "B":
#         print("Falsch, Beginnt mit Unterstrich, was häufig für interne Variablen benutzt wird.")
#     elif antwort == "D":
#         print("Falsch, Beginnt mit Buchstaben, enthält Zahl an späterer Stelle – das ist okay.")
#     elif antwort == "A":
#         print("Falsch so wäre die Variablenname my_var erlaubt und für andere auch perfekt bei der Lesbarkeit")
#     else:
#         print("Falsch")

# frage1()

zahlen_liste = [3, 3, 1, 4, 3, 2, 1]

einzigartige_Ganze_Zahlen = set(zahlen_liste)
print(einzigartige_Ganze_Zahlen)

print(sum(zahlen_liste))
print(len(zahlen_liste))

haeufigkeit = {}
for zahl in zahlen_liste:
    haeufigkeit[zahl] = haeufigkeit.get(zahl, 0) + 1

print(haeufigkeit)

for zahl in sorted(haeufigkeit):
    print(f"{zahl}: {haeufigkeit[zahl]}")

