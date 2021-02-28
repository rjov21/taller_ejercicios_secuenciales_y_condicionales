# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 12:46:15 2021

@author: DIOS BENDITO
"""

# ejercico 1
persona1 = int(input('ingrese la cantidad invertida por la persona 1: '))
persona2 = int(input('ingrese la cantidad invertida por la persona 2: '))
persona3 = int(input('ingrese la cantidad invertida por la persona 3: '))
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

# ejercicio 4
cantidad_metros = int(input('ingrese la cantidad de metros a comprar: '))
valor = cantidad_metros * 80000
cuota_inicial = valor * 0.35
cuotas = (valor - cuota_inicial) / 12
print(f'el valor de la cuota inicial es: {cuota_inicial}')
print(f'el valor de las cuotas es: {cuotas}')

# ejercicio 5
sueldo = int(input('ingrese el sueldo del empleado: '))
politica_publica = sueldo * 0.1
seguro_social = sueldo * 0.4
seguro_forzoso = sueldo * 0.005
caja_ahorro = sueldo * 0.5
print(f'el valor del descuento por politica publica es: {politica_publica}')
print(f'el valor del descuento por seguro social es: {seguro_social}')
print(f'el valor del descuento por seguro forzoso es: {seguro_forzoso}')
print(f'el valor del descuento por caja ahorro es: {caja_ahorro}')
monto_final = politica_publica + seguro_social + seguro_forzoso + caja_ahorro + sueldo
print(f'el monto final a pagar al empleado es: {monto_final}')

# ejercicio 6
palabras = int(input('ingrese la cantidad de palabras: '))
centimetros = int(input('ingrese la cantidad de centimetros: '))
colores = int(input('ingrese la cantidad de colores: '))
valor_palabras = palabras * 20000
valor_centimetros = centimetros * 15000
valor_colores = colores * 25000
valor_final = valor_palabras + valor_centimetros + valor_colores
print(f'el monto a pagar es: {valor_final}')

# ejercicio 7
años = int(input('ingrese los años del empleado: '))
sueldo = int(input('ingrese el sueldo del empleado: '))
bonificacion = años * 120000
sueldo_final = bonificacion + sueldo
print(f'el sueldo final del empleado es: {sueldo_final}')

# ejercicio 8
horas = int(input('ingrese las horas del profesor: '))
monto = horas * 20000
descuento = monto * 0.5
monto_final = monto + descuento
print(f'el descuento a pagar al profesor es: {descuento}')
print(f'el monto a pagar al profesor es: {monto_final}')

# ejercicio 9
monto_inicial = int(input('ingrese el monto inicial: '))
monto_final = int(input('ingrese el monto final: '))
costo_llamada = monto_final - monto_inicial
print(f'el costo de la llamada es: {costo_llamada}')

# ejercicio 10
fotos = int(input('ingrese el numero de fotos del rollo: '))
valor_rollo = fotos * 1500
valor_iva = valor_rollo * 0.16
valor_final = valor_rollo + valor_iva
print(f'el valor completo del revelado es: {valor_final}')
