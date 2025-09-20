# crear un programa que reciba 4 numeros 
# que muestra la suma de los dos primeros
# la multiplicacion de los dos ultimos
# la resta del primero y el cuarto
# y la division entre el tercero y el segundo

# introducir los datos
a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))
c = int(input("Ingrese el tercer numero: "))
d = int(input("Ingrese el cuarto numero: "))

# realizar los procesos y operaciones
suma = a + b
multiplicacion = c * d
resta = a - d
division = c / b

# mostrar los resultados
print("La suma de los dos primeros es: ", suma)
print("La multiplicacion de los dos ultimos es: ", multiplicacion)
print("La resta del primero y el cuarto es: ", resta)
print("La division entre el tercero y el segundo es: ", round(division, 2))