#operadores logicos 'AND'

ganaMucho = False
creditStatus = True

if ganaMucho and creditStatus:
    print('Puede solicitar el prestamo')
else:
    print('No puede solicitar el prestamo')

#operador logico 'OR'

if ganaMucho or creditStatus:
    print('Puede solicitar el prestamo')
else:
    print('No puede solicitar el prestamo')

#operador logico 'NOT' invierte cualquier valor booleano que le proporcionemos

esCriminal = False

if creditStatus and not esCriminal:
    print('Puede solicitar el prestamo')
else:
    print('No puede solicitar el prestamo')

#operadores de comparacion '<', '>', '==', '>=', '<=', '!='

temperatura = 30

if temperatura > 30:
    print('Hace calor')
else:
    print('no hace calor')