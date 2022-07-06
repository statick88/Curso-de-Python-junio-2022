class Usuario:
    def __init__(self, nombre, apellido):  
        self.nombre = nombre
        self.apellido = apellido
        
    def saludo(self):
        print("Hola, mi nombre es", self.nombre, self.apellido)

class Admin(Usuario):
    
    def superSaludo(self):
        print("Soy el administrador del Sistema")
    
usuario = Usuario("Juan", "Martinez")

usuario.saludo()
persona = Usuario("Juan", "Martinez")
persona.saludo()

administrador = Admin("Adminitrador", "Sistemas")
administrador.superSaludo()