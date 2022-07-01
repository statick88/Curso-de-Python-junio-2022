"""persona1 = {
    "name": "Martin",
    "telefono": 2571545
}
print(persona1)
print(persona1["telefono"])
print(persona1.get("name"))

persona1["name"] = "Juan"
print(persona1["name"])
print(persona1)

print(len(persona1))

persona1["ciudad"] = "Loja"
print(persona1)

persona1.pop("ciudad")
print(persona1)

persona1.popitem()
print(persona1)

del persona1["name"]
print(persona1)"""

"""persona1 = {
    "name": "Martin",
    "telefono": 2571545
}
persona2 = {
    "name": "Juan",
    "telefono": 2571000
}
#print(persona1, persona2)
lista = [persona1["name"], persona2["name"]]
print(lista)"""

"""perros = {
  "Tobby":{
    "name": "Tobby",
    "age": 6
    },
  "Leo":{
    "name": "Leo",
    "age": 1
    }
}
print(perros)"""

Rocky = dict(name="Rocky", age=2)
Leo = dict(name="Leo", age=1)
Tobby = dict(name="Tobby", age=6)
perritos={"Rocky":Rocky, "Leo":Leo, "Tobby":Tobby}
print(perritos)