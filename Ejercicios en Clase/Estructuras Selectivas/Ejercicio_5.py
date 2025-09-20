# dado el año en que nacio una persona
# indicar si es mayor o menor de edad

anio_nacimiento = int(input("Ingrese su año de nacimiento: "))
edad = 2025 - anio_nacimiento

if edad >= 18: # camino del SI
    print(f"Usted es mayor de edad, tiene {edad} años")
    
else: # camino del NO
    print(f"Usted es menor de edad, tiene {edad} años")