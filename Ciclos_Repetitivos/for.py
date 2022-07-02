personas = ["Juan","Pedro", "Luisa"]
persona = 0
for persona in personas:
    print(persona)

nombre = "Juan"
for i in nombre:
    if i == "a":
        continue
    print(i)
"""limite = int(input("Por favor ingrese el límite: "))
for i in range(0, limite):
    print(i)


"""

verduras = ["Lechuga", "Brocoli", "Zanahoria", "Remolacha", "Col"]

for verdura in verduras:
    if verdura != "Zanahoria":
        pass
    print(verdura)