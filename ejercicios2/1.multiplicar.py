"""
Multiplicar 2 números sin usar el simbolo de teclado
"""
"""
Paso 1 - Declarar 2 números
Paso 2 - Iterar sobre un número y subar el número opuesto.
"""
from curses import reset_shell_mode


a = 9
b = 4
respuesta = 0
for x in range(a):
    respuesta += b
    
print(respuesta) 