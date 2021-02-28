# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 16:57:19 2021

@author: DIOS BENDITO
"""

# ejercicio 1
cantidad = int(input('ingrese la cantidad de camisetas: '))
valor = int(input('ingrese el valor de las camisetas: '))
if cantidad >= 3:
    descuento = (valor * cantidad) * 0.3
else:
    descuento = (valor * cantidad) * 0.1
monto_final = (valor * cantidad) - descuento
print(f'el monto final a pagar es: {monto_final}')

# ejercicio 2
numero = int(input('ingrese el numero: '))
total_compra = int(input('ingrese el valor total de la compra'))
if numero < 74:
    descuento = (total_compra * 0.15)
else:
    descuento = (total_compra * 0.2)
monto_final = total_compra - descuento
print(f'el valor total a pagar por la compra es: {monto_final}')
