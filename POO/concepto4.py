class Persona:

    def __init__(self):
        #self.nombre = nombre
        pass

    def caminar(self):
        return "Yo soy una persona y puedo caminar" #self.nombre

    def conducir(self):
        return "Yo soy una persona y puedo conducir" #self.nombre

Maria = Persona()
Juan = Persona()

print(Maria.caminar())
print(Juan.conducir())