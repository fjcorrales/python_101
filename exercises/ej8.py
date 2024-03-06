###Ejercicio, hacer uso de bucles anidados para poder imprimir:
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
str = ''
for item in numbers:
    for i in range(item):
        str += 'x'
    print(str)
    str = ''