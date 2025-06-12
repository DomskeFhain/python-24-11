# Debug 1
# def begrüßung(name):
#     print("Hallo" , name)
# begrüßung("Suheib")
# Frage: Warum funktioniert dieser Funktionsaufruf nicht?

# Debug 2
# def addiere(x, y=0, z=0):
#     return x + y + z
# Frage: Warum akzeptiert Python diese Funktionsdefinition nicht?

# Debug 3
# x = "global"
# def test():
#     global x
#     x = "lokal"
# test()
# print(x)
# Frage: Warum bleibt x beim Wert “global”? Wie könnte man x innerhalb der Funktion global verändern?

# Debug 4
# def rechne(a, b):
#     try:
#         return a / b
#     except ZeroDivisionError:
#         return "Du darfst nicht durch 0 teilen"
# print(rechne(5, 0))
# Frage: Warum wird nichts zurückgegeben? Wie könnte man das verbessern?

# Debug 5
# def teile(x, y):
#     if y == 0:
#         raise ZeroDivisionError("Teilen durch Null ist nicht erlaubt")
#     return x / y
# try:
#     teile(4, 0)
# except ZeroDivisionError as e:
#     print("Fehler aufgetreten:", e)
# Frage: Ist die Fehlerbehandlung hier sinnvoll? Was fehlt in der Fehlermeldung?

# Debug 6
# def mache_etwas():
#     try:
#         x = int("1")
#     finally:
#         print("Fertig")
# mache_etwas()
# Frage: Was passiert hier und warum wird kein Fehler angezeigt?

# Debug 7
# def berechne():
#     try:
#         return 10 / 0
#     except ZeroDivisionError:
#         print("Fehler")
#     finally:
#         return "Fertig"
# print(berechne())
# Frage: Warum wird “Fertig” zurückgegeben und nicht “Fehler”? Was ist der Einfluss von finally?

# Debug 8
# def konvertiere(zahl):
#     try:
#         return int(zahl)
#     except ValueError:
#         print("Ungültige Eingabe")
# x = konvertiere("abc")
# print(x + 1)

# Frage: Warum gibt es einen neuen Fehler, obwohl der erste abgefangen wurde?