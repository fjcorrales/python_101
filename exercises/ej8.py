###Ejercicio, hacer uso de bucles anidados para poder imprimir el dibujo de la siguiente F:
#
# xxxxx
# xx
# xxxxx
# xx
# xx ###

numbers = [5, 2, 5, 2, 2]

#sin bucle anidado
for mult in numbers:
    print(mult*'x')

print('\n')

#con bucle anidado, el truco es que en python puedes sumar con strings
for item in numbers:
    str = ''
    for i in range(item):
        str += 'x'
    print(str)