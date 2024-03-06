precio = 1000000
creditStatus = False

if creditStatus:
    porcentaje = precio*0.1
else:
    porcentaje = precio*0.2

print(f'Ha de depositar por adelantado {porcentaje}$')
