# Ejercicio 1 de Matrices
# Crear una matriz NxN y realizar las siguientes operaciones:
# 1. Imprimir la matriz completa.
# 2. Imprimir la suma de todos los elementos.
# 3. Imprimir la diagonal principal.

# definir el tamaño de la matriz
N = int(input("Ingrese el tamaño N de la matriz NxN: "))

# Crear una matriz NxN con valores del 1 al N*N
matriz = []
contador = 1
for i in range(N):
    fila = []
    for j in range(N):
        fila.append(contador)
        contador += 1
    matriz.append(fila)

# 1. Imprimir la matriz completa
print("Matriz completa:")
for fila in matriz:
    print(fila)

# 2. Imprimir la suma de todos los elementos
suma_total = 0
for fila in matriz:
    for columna in fila:
        suma_total += columna
print(f"Suma de todos los elementos: {suma_total}")

# 3. Imprimir la diagonal principal
print("Diagonal principal:")
for i in range(N):
    print(matriz[i][i], end=' ')