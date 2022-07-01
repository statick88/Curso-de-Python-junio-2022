dato = input("Por favor ingrese algo: ")

#print(dato)

lista = ["Hola","Mundo"]
    
if lista.count(dato) > 0:
    print("Esta información existe:", dato)
else:
    print("Esta información no existe", dato)