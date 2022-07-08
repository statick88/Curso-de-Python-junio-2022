archivo = open("nombres.txt", "w")

archivo.write("\nagregamos un ejemplo de nueva línea")
archivo.close()

archivo = open("nombres.txt", "r")
print(archivo.read())


