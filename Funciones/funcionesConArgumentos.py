"""
Fuinciones con argumentos
"""

"""def nombre(nombre):
    print("Bienvenido a Python", nombre)

nombre("Diego")"""

"""def nombre(nombre, apellido):
    print("Bienvenido a Python", nombre, apellido)

nombre("Diego","Saavedra")"""

"""def nombre(*nombre):
    print("Bienvenido a Python", nombre)

nombre("Diego","Saavedra")"""

"""def nombre(*nombre):
    print("Bienvenido a Python", nombre[0])

nombre("Diego","Saavedra")"""

"""def nombre(apellido, nombre):
    print("Bienvenido a Python", nombre, apellido)

nombre(nombre="Diego",apellido="Saavedra")"""

"""def nombre(**kwargs):
    print(kwargs["nombre"],kwargs["apellido"])

nombre(nombre="Diego",apellido="Saavedra")"""

"""def nombre(nombre="Diego", apellido="Saavedra"):
    print("Su nombre es:", nombre, apellido)

nombre()
nombre(nombre="Diego",apellido="Saavedra")
nombre(nombre="Juan",apellido="Perez")
nombre("Juan","Perez")
"""

"""def nombre(lista):
    for nombre in lista:
        print(nombre)

nombre(["Diego","Medardo","Saavedra","Garcia"])"""

"""nombre=input("Nombre: ")
apellido=input("Apellido: ")

def nombrePersona(lista):
    for nombre in lista:
        print(nombre)

nombrePersona([nombre, apellido])"""

"""def paises(pais):
    return pais

print(paises("Ecuador"))"""

"""variable = "Diego"
print(variable)

def nombre(persona):
    global variable
    print(variable)

nombre("Juan")
print(variable)"""

