# Leer una frase y mostrar por pantalla la
# cantidad de vocales

a = 0
e = 0
i = 0
o = 0
u = 0

frase = input("Ingrese una frase: ")
for caracter in frase:
    if caracter.lower() == 'a':
        a += 1
    elif caracter.lower() == 'e':
        e += 1
    elif caracter.lower() == 'i':
        i += 1
    elif caracter.lower() == 'o':
        o += 1
    elif caracter.lower() == 'u':
        u += 1
        
print(f"Cantidad de vocales:\nA: {a}\nE: {e}\nI: {i}\nO: {o}\nU: {u}")