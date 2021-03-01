# ejercicio 1
cantidad = int(input('ingrese la cantidad de camisetas'))
valor = int(input('ingrese el valor de camiseta'))
if cantidad >= 3:
    descuento = (valor * cantidad) * 0.3
else:
    descuento = (valor * cantidad) * 0.1
valor_final = valor - descuento
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
