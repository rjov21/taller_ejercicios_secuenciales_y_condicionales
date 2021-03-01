# ejercicio 1
cantidad = int(input('ingrese la cantidad de camisetas: '))
valor = int(input('ingrese el valor de camiseta: '))
if cantidad >= 3:
    descuento = (valor * cantidad) * 0.3
else:
    descuento = (valor * cantidad) * 0.1
valor_final = (valor * cantidad) - descuento
print(f'el valor final a pagar es: {valor_final}')

# ejercicio 2
numero = int(input('ingrese el numero: '))
total_compra = int(input('ingrese el total de la compra: '))
if numero < 74:
    descuento = total_compra * 0.15
else:
    descuento = total_compra * 0.2
total_final = total_compra - descuento
print(f'el total a pagar por la compra es: {total_final}')

# ejercicio 3
monto = int(input('ingrese el monto: '))
if monto < 50000:
    cuota = monto * 0.03 
else:
    cuota = monto * 0.02
print(f'la cuota que debe pagar la afianzadora es: {cuota}')

# ejercicio 4
promedio_puntos = int(input('ingrese el promedio de puntos de la semana: '))
ganancia_dia = int(input('ingrese las ganacias darias: '))
if promedio_puntos >170:
    perdida = (ganancia_dia * 5) * 0.5
else:
    print('no habra perdida')
print(f'la fabrica perdera {perdida} en la semana ')

# ejercicio 5
valor_carro = int(input('ingrese el valor del carro: '))
valor_terreno = valor_carro
devaluacion = valor_carro * 0.3
incremento = valor_terreno * 0.45
if devaluacion < incremento:
    print('debe comprar el carro')
else:
    print('debe comprar el terreno')

# ejercicio 6
cantidad = int(input('ingrese la cantidad de computadoes: '))
valor = 11000
if cantidad < 5:
    descuento = (valor * cantidad) * 0.1
elif cantidad >= 5 and cantidad < 10:
    descuento = (valor * cantidad) * 0.2
else:
    (valor * cantidad) * 0.4
valor_final = (valor * cantidad) - descuento
print(f'el valor final a pagar es: {valor_final}')

# ejercicio 7
valor = int(input('ingrese el valor del producto: '))
marca = input('ingrese la marca del producto: ')
if valor >= 2000:
    valor_final = (valor - (valor * 0.1)) + (valor * 0.16)
elif marca == 'NOSY':
    valor_final = (valor - (valor * 0.05)) + (valor * 0.16)
else:
    valor_final = valor + (valor * 0.16)
print(f'el valor final a pagar por el producto es: {valor_final}')
