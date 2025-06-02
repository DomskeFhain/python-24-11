# def hallo(name,nachname):
#     print("Hallo " + name + " " + nachname)

# hallo("Senda", "Zidi")
# hallo("Marcus", "Vix")

# def addieren(zahl1, zahl2):
#      return zahl1 + zahl2

# ergebnis = addieren(3,4)

# print("Das ergebnis ist: " + str(ergebnis))


### Generator
# import random
# def zahlen():
#     yield random.randint(1,10)
#     yield random.randint(1,10)
#     yield random.randint(1,10)

# # generator = zahlen()
# # print(next(generator))
# # print(next(generator))
# # print(next(generator))

# for zahl in zahlen():
#     print(zahl)

# for zahl in zahlen():
#     print(zahl)


##### Rekursion
# def fakultät_ohne_rekursion(zahl):
#     faktor = 1
#     for i in range(1,zahl+1):
#         faktor *= i
#     return faktor

# print(fakultät_ohne_rekursion(7))

# def fakultät_mit_rekursion(zahl):
#     if zahl == 0:
#         return 1
#     else:
#         return zahl * fakultät_mit_rekursion(zahl-1)

# print(fakultät_mit_rekursion(7))

# def fibbonacci(zahl):
#     if zahl == 0:
#         return 0
#     elif zahl == 1:
#         return 1
#     else:
#         return fibbonacci(zahl-1) + fibbonacci(zahl-2)
    
# print(fibbonacci(34))

## Parameter: Platzhalter in der Funktionsdefinition
## Argumente: Die echten Werte beim aufruf der funktion

# def hallo(name,nachname): # name, nachname sind die Paramter
#     print("Hallo " + name + " " + nachname)

# # hallo("Senda", "Zidi") # Senda, Zidi sind die Argumente
# # hallo("Marcus", "Vix") # Marcus, Vix sind die Argumente

# hallo("Joshua","Anders") ## Positionsargumente
# hallo(nachname="Anders",name="Joshua") ## Schlüsselwortargument
# hallo("Joshua",nachname="Anders") ## gemischte Argumente ## schlüsselwortargumente müssen hinten sein

# def begrueßung(name="Gast"):
#     print("Hallo "+ name)

# begrueßung("Suheib")

# def test():
#     x = 10 # lokale Variable
#     print(x)

# print(x) ## wird nicht funktionieren, da x nur in der Funktion test exisitert

#Shadowing
# x = 5
# def test():
#     x = 10 
#     print(x)
# test() ## 10
# print(x) ## 5

##global
x = 5
def test():
    global x
    x = 10 
    print(x)
test()
print(x)