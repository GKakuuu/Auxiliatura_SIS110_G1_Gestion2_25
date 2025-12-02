# mostrar el ultimo y primer digito de un numero

from math import log10

num = int(input("Introducir un numero entero: "))

cant_digitos = int(log10(num)) + 1
divisor = 10 ** (cant_digitos - 1)
primer_digito = num // divisor
ultimo_digito = num % 10

print(f"El primer digito es {primer_digito} y el ultimo digito es {ultimo_digito}")