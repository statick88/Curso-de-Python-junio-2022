class Deportes:

    def __init__(self, nombre, balon):
        self.nombre = nombre
        self.instrumento = balon

Baloncesto = Deportes("Baloncesto", "Balon de Baloncesto")
Futbool = Deportes("Baloncesto", "Balon de Futbool")
Tenis = Deportes("Baloncesto", "Balon de Tenis")

print(Baloncesto.nombre)
print(Tenis.instrumento)