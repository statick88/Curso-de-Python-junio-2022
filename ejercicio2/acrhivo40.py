palabra = input("Ingrese una palabra: ") 
vocales = ["a", "e", "i", "o", "u", "á", "é", "í", "ó", "ú", "A", "Á"] 
i = 0 
for x in vocales: 
    for j in palabra: 
        if x == j: 
            i+=1 
            
print ("El número de vocales es: ",i) 