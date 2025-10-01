# Ejercicio 3:
# Escribir un programa que pida un número entero y
# muestre por pantalla el primer y el último dígito.
# trabajar sin strings, trabajar con matematicas (logaritmos, divisiones, modulos)
# entrada       salida
# 4             4 4 
# 24            2 4
# 334589        3 9
# 9876543210    9 0

from math import log10

num = int(input("Ingrese un numero entero: "))
cant_digitos = int(log10(num)) + 1
divisor = 10 ** (cant_digitos - 1)
primer_digito = num // divisor  # obtener el primer digito
ultimo_digito = num % 10        # obtener el ultimo digito

print(f"El primer digito es {primer_digito} y el ultimo digito es {ultimo_digito}")