# Leer una matriz de 5x5 y mostrar por
# pantalla el promedio de cada fila.

Matriz = []
promedios = []

print("Ingrese los 5 números de las diferentes filas separados por espacios: ")
for i in range(5):
    fila = str(input(f"Fila {i+1}: "))
    numeros_fila = list(map(int, fila.split()))
    Matriz.append(numeros_fila)
    suma_fila = (sum(numeros_fila)) / 5
    promedios.append(suma_fila)

print("Promedios de cada fila:")
print(promedios)
for num in promedios:
    print(f"{num:.2f}", end=' ')