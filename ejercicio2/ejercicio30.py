#Ingresar nombre y aplellido e imprimirlo alreves 

dato = input("Ingrese nombre y apellido") 
print("Su nombre es:", dato) 

listaNombreApellido = [] 

for recorrido in dato: 
    if recorrido == "cadena": 
        continue 
    listaNombreApellido.append(recorrido) 
    #Codigo para imprimir en reversa 
print(listaNombreApellido) 
i=0 
for Reversa in listaNombreApellido:
    """ultimo = listaNombreApellido.pop() print(ultimo)""" 
    i-=1 
    print(listaNombreApellido[i]) #print(Reversa) 