# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 12:46:15 2021

@author: DIOS BENDITO
"""

# ejercico 1
persona1 = int(input('escriba la cantidad invertida por la persona 1: '))
persona2 = int(input('escriba la cantidad invertida por la persona 2: '))
persona3 = int(input('escriba la cantidad invertida por la persona 3: '))
cantidad_total = persona1 + persona2 + persona3
cantidad_invertida_persona1 = (persona1 * 100) / cantidad_total
cantidad_invertida_persona2 = (persona2 * 100) / cantidad_total
cantidad_invertida_persona3 = (persona3 * 100) / cantidad_total
print(f'el % invertido por persona1 es: {cantidad_invertida_persona1}%')
print(f'el % invertido por persona2 es: {cantidad_invertida_persona2}%')
print(f'el % invertido por persona3 es: {cantidad_invertida_persona3}%')

# ejercicio 2
sueldo = int(input('ingrese el sueldo del empleado: '))
cantidad_hijos = int(input('ingrese la cantidad de hijos del empleado: '))
bonificacion = 80000 * cantidad_hijos
print(f'el valor de la bonificacion es: {bonificacion}')
monto_total = sueldo + bonificacion
print(f'el monto total a pagar al empleado es: {monto_total}')

# ejercicio 3
monto_ahorrado = int(input('ingrese el monto ahorarrado: '))
monto_final = monto_ahorrado * 1.5
print(f'el monto final es: {monto_final}')
