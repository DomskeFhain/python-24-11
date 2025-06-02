person = {
    "name":"Christof",
    "alter": 29,
    "schulfächer": {"Mathe":1,"Physik":3}
}

person["alter"] = 35
print(person["alter"])
print(person["schulfächer"])
print(person.get("alter"))
print(person["schulfächer"]["Mathe"])

person["hobby"] = "Programmieren"
print(person)

print("-------------------")

# del person["hobby"]
# print(person)

# person.pop("alter")
# print(person)

# person.clear()
# print(person)

for abc in person.items(): # abc ist nur ein platzhalter
    print(abc)

for abc in person.keys():
    print(abc)

for abc in person.values():
    print(abc)

print(person.items())
print(person.keys())
print(person.values())

print("alter" in person)
print("lieblingsessen" not in person)