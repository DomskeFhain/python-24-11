# print("Banana"*3)
# string1 = "Hallo ich bin ein String"
# string2 = 'Hallo ich bin auch ein String'

# print(string1[0])
# print(string1[-1])
# print(string1[0:5]) # Hallo

# # string1[0] = "J" ## immutable
# string1 = "Hallo" ## das geht aber

# print(string1)

# string3 = "Mein Lieblingswort ist 'Programmieren' "
# ## mit backslash(escape-zeichen) maskieren wir die Anführungszeichen
# string4 = "Mein Lieblingswort ist \" Programmieren \" "
# print(string3)
# print(string4)

# string5 = """Hallo   
# mein
#                 name  
# ist"""
# print(string5)

mein_string = "hallo was geht"
print(len(mein_string))
print(mein_string.upper())
print(mein_string.lower())

# user_eingabe  = input("wann bist du geboren ?:")

# if user_eingabe.lower() == "januar":
#     print("Dein Geburtsmonat ist Januar")

print("Python".lower()) # Alle Buchstaben klein 
print("Python".upper()) # Alle Buchstaben groß
print("python".capitalize()) # Erster Buchstabe groß

print("Banana".replace("a","x")) # Zeichen ersetzen, in dem fall alle a´s durch x ersetzen
print("das ist der heutige titel".title()) # Erster Buchstabe der Worte groß
print("das ist der heutige titel".split()) ## erstellt eine Liste aus den Wörtern
print(" ".join(["hallo","was","geht"])) # erstellt einen String aus einer Liste getrennt vom Zwischenzeichen
print("     Ich bin ein komisch formattierter String           ".strip()) # entfernt Leerzeichen am anfang und am ende des Strings
print("     Ich bin ein komisch formattierter String           ".rstrip()) # entfernt Leerzeichen  am ende des Strings
print("     Ich bin ein komisch formattierter String           ".lstrip()) # entfernt Leerzeichen am anfang des Strings
