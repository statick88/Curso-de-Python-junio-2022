primerNumero = input("Ingrese el primer número: ")

try:
    primero = int(primerNumero)
except:
    primero = "Cadena"

segundoNumero = input("Ingrese el segundo número: ")

try:
    segundo = int(segundoNumero)
except:
    segundo = "algo"

if primero == "Cadena" or segundo == "algo":
    print("Ingreso mal un dato, pruebe por favor una vez mas ingresando numeros")
else:
    print(primero + segundo)