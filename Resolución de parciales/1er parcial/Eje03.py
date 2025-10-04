# leer dos numeros y mostrar el mayor de
# los primeros digitos
# entrada     salida
# 17 58       5

from math import log10

a = int(input("introducir el primer numero: "))
b = int(input("introducir el segundo numero: "))

mayor = max(a , b)

cant_digitos = int(log10(mayor)) + 1
divisor = 10 ** (cant_digitos - 1)
primer_digito = mayor // divisor

print(f"El primer digito es {primer_digito}")