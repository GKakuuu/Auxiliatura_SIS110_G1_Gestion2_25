# verificar si un numero es par o impar
# en caso de que el numero sea par sumarle el doble
# en caso de que sea impar restarle la mitad

numero = int(input("Ingrese un numero: "))
if numero % 2 == 0: # camino del SI
    print(f"El numero {numero} es par")
    numero += numero * 2
    # 10 + 10 * 2 = 30
    print(f"El nuevo valor del numero es: {numero}")
else: # camino del NO
    print(f"El numero {numero} es impar")
    numero -= numero / 2
    # 11 - 11 / 2 = 5.5
    print(f"El nuevo valor del numero es: {numero}")

