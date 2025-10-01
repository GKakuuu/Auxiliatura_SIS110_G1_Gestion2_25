# Ejercicio 1:
# Escribir un programa que pida un número entero y
# muestre por pantalla la cantidad de dígitos que tiene.

# entrada       salida
# 4             1   
# 24            2
# 334589        6
# 9876543210    10

from math import log10

num = int(input("Ingrese un numero entero: "))

if num == 0:
    print(f"El numero {num} tiene 1 digito")
else:
    cant_digitos = log10(abs(num)) + 1
    print(f"El numero {num} tiene {int(cant_digitos)} digitos")