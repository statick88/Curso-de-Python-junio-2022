"""
Crear una clase perro y crear 2 instancias Tobby y Leo
"""
class Perro:
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza

    def ladrar(self):
        return "Yo soy", self.nombre, "y mi raza es: ", self.raza

    def comer(self):
        return "Yo como croquetas"

Tobby = Perro("Tobby", "Runa")
print(Tobby.ladrar())

Leo = Perro("Leo", "Runa")
print(Leo.ladrar())
print(Leo.comer())