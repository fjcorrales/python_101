#haremos uso de algunas de las librerias predefinidas con las que viene python
#se pueden buscar las diferentes librerias estandar de pyhton en google https://docs.python.org/3/py-modindex.html
#aasimismo se puede acceder a la pagina https://pypi.org/ para buscar librerias utiles
#vamos a usar la libreria 'random' que nos permite generar valores aleatorios

#dado que random es un modulo integrado no es necesario que tengamos un fichero en nuestro proyecto
#se encuentra en la carpeta de external libraries -> python3 library root en alguna parte de nuestro pc, viene con python
import random

miembros = ['Jhon', 'Maria', 'Juan', 'Carlos']

for i in range(3):
    print(random.random())  #esta es la funcion random() base que nos genera un numero aleatorio entre 0 y 1


print('\n')

for i in range(3):
    print(random.randint(1, 10))  #esta es la funcion random() base que nos genera un numero aleatorio entre 2 valores especificados


print('\n')

lider = random.choice(miembros) #esta funcion nos permite elegir un valor aleatorio de una lista
print(lider)
