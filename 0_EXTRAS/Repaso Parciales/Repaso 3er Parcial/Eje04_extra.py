# escribir una funcion para contar las letras mayusculas de una cadena
def contar_mayusculas(cadena):
    contador = 0
    for letra in cadena:
        if letra.isupper():
            contador += 1
    return contador

# probar la funcion
cadena = "Hola Mundo! Esto Es Una Prueba."
resultado = contar_mayusculas(cadena)
print(f"La cantidad de letras mayusculas en la cadena es: {resultado}")