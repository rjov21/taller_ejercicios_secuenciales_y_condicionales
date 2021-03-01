monto = int(input('ingrese el monto: '))
if monto < 50000:
    cuota = monto * 0.03 
else:
    cuota = monto * 0.02
print(f'la cuota que debe pagar la afianzadora es: {cuota}')
