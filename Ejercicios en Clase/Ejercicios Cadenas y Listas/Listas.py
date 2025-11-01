list_num = [1, 2, 3, 4, 5]
list_str = ['a', 'b', 'c', 'd', 'e']

# # Acceder a elementos
# for i in range(len(list_num)):
#     print(f'Elemento en índice {i} de list_num: {list_num[i]}')
#     print(f'Elemento en índice {i} de list_str: {list_str[i]}')

# for element in list_num:
#     print(f'Elemento de list_num: {element}')
# for element in list_str:
#     print(f'Elemento de list_str: {element}')

# Métodos de listas
list_num.append(6)  # Agrega un elemento al final
list_str.append('f')  # Agrega un elemento al final
print("Después de append:", list_num, list_str)

list_num.remove(3)  # Elimina el primer elemento con valor 3
list_str.remove('c')  # Elimina el primer elemento con valor 'c'
print("Después de remove:", list_num, list_str)

list_num.insert(2, 10)  # Inserta 10 en el índice 2
list_str.insert(2, 'z')  # Inserta 'z' en el índice 2
print("Después de insert:", list_num, list_str)

list_num.sort()  # Ordena la lista numéricamente
list_str.sort()  # Ordena la lista alfabéticamente
print("Después de sort:", list_num, list_str)

list_num.reverse()  # Invierte el orden de la lista
list_str.reverse()  # Invierte el orden de la lista
print("Después de reverse:", list_num, list_str)

list_num.pop()  # Elimina y devuelve el último elemento
list_str.pop()  # Elimina y devuelve el último elemento

print("Después de pop:", list_num, list_str)

list_num.extend([7, 8, 9])  # Extiende la lista con múltiples elementos
list_str.extend(['g', 'h', 'i'])  # Extiende la lista con múltiples elementos
print("Después de extend:", list_num, list_str)

list_num.clear()  # Elimina todos los elementos de la lista
list_str.clear()  # Elimina todos los elementos de la lista
print("Después de clear:", list_num, list_str)
