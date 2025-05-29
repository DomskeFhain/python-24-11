## Debug 1
zahl = "10" ## Anführungszeichen sind falsch - "10" <-- so ist es richtig, ist jetzt aber auch nen string und das Ergebnis wäre 105  
ergebnis = zahl + 5
print(ergebnis)


## Debug 2 
x = 3
if x > 0:
    print("x ist positiv") ## Anführungszeichen sind falsch und endlosschleife sowie auch einrückungfehler war da - "x ist positiv" 


## Debug 3 
for i in range(5):
    print(i)    ## einrückungsfehler


## Debug 4 
alter = 18
if alter >= 18:
    print("Volljährig") ## Anführungszeichen sind falsch und einrückungsfehler sowie auch > hat gefehlt


## Debug 5
x = 4
y = 2
z = x ^ y
print("Ergebnis ist", z)
## Was passiert hier nochmal ? Was ist ^? Hinweis: Bitweise Operatoren


## Debug 6
x = 10
if x > 0:
    if x < 5:
        print("klein")
else:
    print("groß")


## Debug 7
while True:
    eingabe = input("Soll ich 'Hallo' ausgeben? (j/n): ")
    if eingabe.lower() != "j":
        break
    print("Hallo")
## Hinweis: Endlosschleife 

## Debug 8

eingabe = input("Gib eine Zahl ein: ")
if eingabe > 10:
    print("größer als 10")