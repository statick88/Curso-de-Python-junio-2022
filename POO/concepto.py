"""
Clase <---
Objeto <---
Atributo <---
Metodo <---
"""
class Moster:
    def __init__(self, nombre, categoria):
        self.nombre = nombre
        self.categoria = categoria

    def myfunc(self):
        print("Hey, yo soy "+self.nombre)

mountrito = Moster("Sullivan","Asustador")
mountrito.myfunc()
print(mountrito.categoria)
