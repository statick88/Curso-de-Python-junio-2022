"""lista = []
print(lista)
"""
lista = ["Juan", "Pedro", "Maria"]
print(lista)
"""
lista = ["Juan", "Pedro", 5, True, ["a","e","i","o","u"]]
print(lista)"""

lista.append("Juana")
print(lista)

"""lista.clear()
print(lista)"""

lista2 = lista.copy()
print(lista2)
print(lista == lista2)

lista2.append("Marcos")
lista2.append("Marcos")
lista2.append("Marcos")
lista2.append("Marcos")
lista2.append(8)

print(lista, lista2)

print(lista == lista2)

print(lista2.count("Juana"))
print(lista2.count("Marisol"))

print(len(lista2))
print(lista2)

print(lista)
print(lista[0])
print(lista[2])

print(lista)
lista.pop()
print(lista)
#lista.pop()
#print(lista)
lista.remove("Pedro")
print(lista)

lista = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(lista)
lista.reverse()
print(lista)

lista = ["q","w","e","r","t","y","u","i","o","p","ñ","l","k","j","h","g","f","d","s","a","z","x","c","v","b","n","m"]
print(lista)
lista.sort()
print(lista)

lista = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(lista)
lista.sort()
print(lista)

lista = ["a","A"]
print(lista)
lista.sort()
print(lista)

