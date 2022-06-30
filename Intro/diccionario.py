persona1 = {
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
print(persona1)