# Leer 10 enteros y mostrar por pantalla el
# promedio y todos los valores mayores al
# promedio.

suma = 0
numeros = []

for _ in range(10):
    num = int(input("Ingrese un número entero: "))
    numeros.append(num)
    suma += num

promedio = suma / 10
print(f"Promedio: {promedio}")

print("Números mayores al promedio:")
for num in numeros:
    if num > promedio:
        print(num, end=' ')
