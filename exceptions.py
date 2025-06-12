# import sys
# counter = 0
# while True:
#     counter += 1
    # if counter == 10:
    #     sys.exit() ## SystemExit
## Keyboard Interrupt -> Strig + C in der Konsole


# try:
#     print(5/0) ## ZeroDivisionError
# except ArithmeticError: 
#     print("Division durch Null ist nicht erlaubt") 


# print("Hallo ich bin außerhalb des try except Blocks ")
# print(str(123))

# liste = [1,2,3]
# try:
#     print(liste[5])
# except IndexError: # oder LookupError da es die Oberklasse ist
#     print("Hier ist ein Fehler aufgetreten")

# print("Ich bin raus aus dem try except Block")

# daten = {"name":"Jan"}

# try:
#     print(daten["alter"])
# except KeyError: # oder LookupError
#     print("Hier ist ein Fehler aufgetreten")
    

# print("Ich bin raus aus dem try except Block")

# try:
#     # print("3" + 3) # TypeError
#     if [1,2,3] > "abc":
#         print("Hallo aus dem if block")
# except TypeError:
#     print("Hier ist ein Fehler aufgetreten")

# print("Ich bin raus aus dem try except Block")

# try:
#     print(int("Hallo"))
# except ValueError:
#     print("Hier ist ein Fehler aufgetreten")

# print("Ich bin raus aus dem try except Block")

## Die Reihenfolge des exception-Zweig geht von klein nach groß
# try:
#     1/0
# except ZeroDivisionError:
#     print("Hier ist ein Fehler aufgetreten")
# except Exception:
#     print("Hier ist kein Fehler aufgetreten")
######### Weitergabe von Ausnahmen über Funktiongrenzen hinweg
#Variante 1
def berechnen(x,y):
    try:
        return x/y
    except ZeroDivisionError:
        return "Fehler"

print(berechnen(1,0))

# oder Variante 2

def berechnen(x,y):
    return x/y

try:
    print(berechnen(1,0))
except ZeroDivisionError:
    print("Fehler")