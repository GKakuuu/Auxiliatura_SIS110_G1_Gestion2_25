# Ejemplo de un diccionario en Python sobre las notas de estudiantes
notas_estudiantes = {
    "Ana": 85, "Pedro": 92, "Luis": 78, "Marta": 90
}

# # Ejemplos de usos de métodos de diccionarios
# # 1. Acceder a un valor mediante su clave
# nota_ana = notas_estudiantes["Ana"]
# print(f"La nota de Ana es: {nota_ana}")

# # 2. Agregar un nuevo par clave-valor
# notas_estudiantes["Carlos"] = 88
# print("Notas después de agregar a Carlos:", notas_estudiantes) 

# # 3. Actualizar la nota de un estudiante existente
# notas_estudiantes["Luis"] = 80
# print("Notas después de actualizar la nota de Luis:", notas_estudiantes)

# # 4. Eliminar un par clave-valor
# notas_estudiantes.pop("Pedro")
# print("Notas después de eliminar a Pedro:", notas_estudiantes)

# 5. Obtener todas las claves del diccionario
claves = notas_estudiantes.keys()
print("Claves del diccionario:", list(claves))

# 6. Obtener todos los valores del diccionario
valores = notas_estudiantes.values()
print("Valores del diccionario:", list(valores))

# 7. Buscar si una clave existe en el diccionario
existe_marta = "Marta" in notas_estudiantes
print("¿Existe Marta en el diccionario?", existe_marta)

existe_marta = "Pepito" in notas_estudiantes
print("¿Existe Pepito en el diccionario?", existe_marta)
