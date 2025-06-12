# ### Debug 1
# ### Fehler
# def begrüßung(name):
#     print("Hallo" name)
# begrüßung()

# ### Lösung
# def begrüßung(name):
#     print("Hallo", name)

# begrüßung("Maria")

# ### Warum 
# ## Komma hat gefehlt und Funktion ist ohne Argument

# ### Debug 2
# ### Fehler
# def addiere(x, y=0, z):
#     return x + y + z
# ### Lösung
# def addiere(x, y, z=0):
#     return x + y + z
# ### Warum
# ## Die Funktion erlaubt Pflichtelemente erst am Ende

# ### Debug 3
# ### Fehler
# x = "global"
# def test():
#     global x
#     x = "lokal"
# test()
# print(x)

# ### Lösung
# ### Warum
# ## x in der Funktion ist eine lokale Variable. Sie verändert die globale nicht.

# ### Debug 4
# ### Fehler
# def rechne(a, b):
#     try:
#         return a / b
#     except:
#         print("Fehler")
# print(rechne(5, 0))
# ### Lösung
# def rechne(a, b):
#     try:
#         return a / b
#     except ZeroDivisionError:
#         print("Fehler")
#         return None
# print(rechne(5, 0))
# ### Warum
# ## Die Funktion gibt nichts zurück, wenn ein Fehler passiert. Deshalb wird in der Lösung None zurückgegeben jetzt.

# ### Debug 5
# ### Fehler
# def teile(x, y):
#     if y == 0:
#         raise ZeroDivisionError
#     return x / y

# try:
#     teile(4, 0)
# except Exception as e:
#     print("Fehler", e)
# ### Lösung
# def teile(x, y):
#     if y == 0:
#         raise ZeroDivisionError("Division durch Null ist nicht erlaubt")
#     return x / y

# try:
#     teile(4, 0)
# except Exception as e:
#     print("Fehler:", e)
# ### Warum
# ## Die Funktion gibt einen Fehler aus, wenn y == 0

# ### Debug 6
# ### Fehler
# def mache_etwas():
#     try:
#         x = int("abc")
#     finally:
#         print("Fertig")
# mache_etwas()

# ### Lösung
# def mache_etwas():
#     try:
#         x = int("abc")
#     except ValueError:
#         print("Ungültige Eingabe")
#     finally:
#         print("Fertig")
# mache_etwas()

# ### Warum
# ## Die Funktion gibt einen Fehler aus, wenn x = int("abc") ist und finally würde immer ausgeführt werden.

# ### Debug 7
# ### Fehler
# def berechne():
#     try:
#         return 10 / 0
#     except ZeroDivisionError:
#         print("Fehler")
#     finally:
#         return "Fertig"
# print(berechne())
# ### Lösung
# def berechne():
#     try:
#         return 10 / 0
#     except ZeroDivisionError:
#         print("Fehler")
#         return "Problem"
#     finally:
#         print("Fertig") 
# print(berechne())
# ### Warum
# ## finally überschreibt alles, auch ein return aus try oder except. finally ist für Aufräumarbeiten. Wenn du darin return nutzt, ersetzt es alles andere.

# ### Debug 8
# ### Fehler
# def konvertiere(zahl):
#     try:
#         return int(zahl)
#     except ValueError:
#         print("Ungültige Eingabe")
# x = konvertiere("abc")
# print(x + 1)
# ### Lösung
# def konvertiere(zahl):
#     try:
#         return int(zahl)
#     except ValueError:
#         print("Ungültige Eingabe")
#         return 0

# x = konvertiere("abc")
# print(x + 1)
# ### Warum
# ## Die Funktion gibt einen Fehler aus, wenn x = int("abc") ist und wenn ein Fehler passiert, wird nichts zurückgegeben. x = None


x = 7
y = 3
print(x % y)
print(x // y)

