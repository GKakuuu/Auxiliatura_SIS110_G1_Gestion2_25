# Ejercicio 2:
# Crear un programa que pida un número entero y muestre la
# primera mitad de ese número seguida de la segunda mitad.
# Dicho numero siempre tendra una cantidad par de digitos.

# entrada       salida
# 24            2 4
# 334589        334 589
# 9876543210    98765   43210

# trabajar sin strings, trabajar con matematicas (logaritmos, divisiones, modulos)

from math import log10

num = int(input("Ingrese un numero entero: "))
cant_digitos = int(log10(num)) + 1

if cant_digitos % 2 != 0: # controlar que tenga cantidad par de digitos
    print("El numero debe tener una cantidad par de digitos")

else:
    mitad = cant_digitos // 2
    divisor = 10 ** mitad
    primera_mitad = num // divisor
    segunda_mitad = num % divisor

    print(f"La primera mitad es {primera_mitad} y la segunda mitad es {segunda_mitad}")


