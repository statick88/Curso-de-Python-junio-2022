"""
5. escribir una funcion que indique si el usuario es mayor de edad
"""

def esMayor(usuario):
    if usuario.edad > 17:
        return f"Es mayor de edad"
    else:
        return f"Es menor de edad"

class Usuario:

    def __init__(self, edad):
        self.edad = edad

usuario1 = Usuario(15)
usuario2 = Usuario(21)

resultado1 = esMayor(usuario1)
resultado2 = esMayor(usuario2)

print(resultado1)
print(resultado2)