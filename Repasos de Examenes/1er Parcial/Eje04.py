# 1. Escribir un programa para leer dos numeros enteros y
# mostrar por pantalla la cantidad total de simbolos que existen:
# Ejemplo del caso 3:
# * ** * ** *
# * ** * ** *
# * ** * ** * 

# Input     Output
# 1  1      1
# 1  5      7
# 3  5      21

num1 = int(input("Ingrese el primer numero (filas): "))
num2 = int(input("Ingrese el segundo numero (columnas): "))

# calculamos la cantidad de columnas pares e impares
impares = (num2 + 1) // 2
pares = num2 // 2

print("Columnas impares:", impares)
print("Columnas pares:", pares)

# calculamos la cantidad total de simbolos
total_simbolos = num1 * (impares * 1 + pares * 2)

print(f"La cantidad total de simbolos es: {total_simbolos}")