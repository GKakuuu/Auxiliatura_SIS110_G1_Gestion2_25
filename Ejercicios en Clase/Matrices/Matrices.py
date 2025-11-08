# Ejemplo basico de matrices en Python usando listas anidadas

# Crear una matriz 3x3
matriz = [ [1, 2, 3],   # fila 0
           [4, 5, 6],   # fila 1
           [7, 8, 9] ]  # fila 2
#   columna 0  1  2

# Imprimir la matriz
for fila in matriz:
    print(fila)
# Imprimir la matriz elemento por elemento

for fila in matriz:
    for columna in fila:
        print(columna, end='_')
    print()  # Nueva línea después de cada fila

# Acceder a un elemento específico (por ejemplo, el elemento en la fila 2, columna 3)
elemento = matriz[1][2]  # Recuerda que los índices empiezan en 0
print(f'El elemento en la fila 2, columna 3 es: {elemento}')