import os

if os.path.exists("nombres.txt"):
    os.remove("nombres.txt")
    print("El archivo ha sido eliminado exitosamente")
else:
    print("El archivo no existe")