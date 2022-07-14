archivo = open("/home/statick/workspaces/Curso-de-Python-junio-2022/nombres.txt", "w")
archivo.write("\nEsto es un script")
archivo.close()

archivo = open("nombres.txt", "r")
print(archivo.read())
archivo.close()

