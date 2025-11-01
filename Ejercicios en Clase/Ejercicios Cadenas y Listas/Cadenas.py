word = "       Hola mundo, bienvenidos a Python.          "

for letter in word:
    print(letter)

for index in range(len(word)):
    print(word[index], ": ", index)

# pruebas con de metodos de cadenas
print(word.upper()) # convierte a mayusculas
print(word.lower()) # convierte a minusculas

print(word.replace("mundo", "a todos")) # reemplaza una subcadena por otra

print(word.split(" ")) # divide la cadena en una lista usando el separador indicado

print(word.find("Python")) # busca la subcadena y devuelve el indice de la primera aparicion

print("En la cadena ", word, " hay ", word.count("a") , "a") # cuenta cuantas veces aparece un caracter o subcadena

print(word.capitalize()) # convierte la primera letra en mayuscula y las demas en minusculas
print(word.title()) # convierte la primera letra de cada palabra en mayuscula
print(word.strip(".")) # elimina los espacios en blanco al inicio y al final, o el caracter indicado
print(word.strip()) # elimina los espacios en blanco al inicio y al final
print(word.replace(" ", "")) # elimina todos los espacios en blanco de la cadena
