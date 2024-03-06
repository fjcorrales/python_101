#juego de adivinar

numero = 6
intento = int(input('Adivina el numero: '))

while intento != numero:
    if intento != numero:
        print('Numero equivocado')
        intento = int(input('Prueba otra vez: '))
else:
    print('Enhorabuena!')