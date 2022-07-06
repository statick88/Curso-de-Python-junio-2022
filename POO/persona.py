class Usuario:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    
    def saludo(self):
        print("Hola, mi nombre es", self.nombre, self.apellido)
    
persona = Usuario("Juan", "Martinez")

persona.saludo()
print(persona)
del persona
#persona.saludo()
#print(persona)