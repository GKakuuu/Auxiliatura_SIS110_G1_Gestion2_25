# Ejercicio 1:
# Escribir un programa que pida un número entero y
# muestre por pantalla la cantidad de dígitos que tiene.

# entrada       salida
# 4             1   
# 24            2
# 334589        6
# 9876543210    10

num = int(input("Ingrese un numero entero: "))
cant_digitos = len(str(num).replace)
print(f"El numero {num} tiene {cant_digitos} digitos")
