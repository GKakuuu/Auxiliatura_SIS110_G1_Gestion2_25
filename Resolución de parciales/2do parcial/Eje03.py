# Leer una matriz de 5x5 y mostrar por
# pantalla el promedio de cada fila.

Matriz = []
sumas = []

for i in range(5):
    fila = str(input(f"Ingrese los 5 números de la fila {i+1} separados por espacios: "))
    numeros_fila = list(map(int, fila.split()))
    Matriz.append(numeros_fila)
    suma_fila = (sum(numeros_fila)) / 5
    sumas.append(suma_fila)

print("Promedios de cada fila:")
print(sumas)