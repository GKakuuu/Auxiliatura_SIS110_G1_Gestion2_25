# crear un programa que permita calcular el
# Indice de Masa Corporal de una persona

# Entrada     Salida
# a   b       IMC
# 60  1.70    20.8

# peso dado en Kg
# Altura dada en m
peso = float(input("Ingrese su peso en Kg: "))
altura = float(input("Ingrese su altura en metros: "))

imc = peso / (altura ** 2)

print("Su Indice de Masa Corporal es: ", round(imc, 2))