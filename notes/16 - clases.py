#Nos permiten crear "tipos de datos" propios, personalizados, nos permiten modelar conceptos complejos
#Aqui definiremos un tipo de dato llamado punto

class Punto: #siguiendo las convenciones de python en clases la primera letra siempre es mayuscula
    def move(self):
        print('move')

    def draw(self):
        print('draw')

punto1 = Punto() #esto crea una instancia de nuestra clase punto
#las instancias de nuestra clase pueden tener atributos
punto1.x = 10
punto1.y = 20
punto1.draw()   #si ponemos punto1.  y esperamos al autocompletado veremos que salen las funciones que acabamos de declarar dentro de la clase
print(punto1.x)

punto2 = Punto()    #hemos creado un objeto diferente, completamente separado de punto1 y este tiene sus propios atributos pero comparte funciones

#Esta implementacion de clases es incorrecta porque podemos crear un punto sin coordenadas
#print(punto2.x) #esto da error, por lo que lo comento

#Lo que queremos es que cuando creamos un punto, este requiera que se le pasen las coordenadas
#Para esto usamos un metodo llamado 'constructor'
class PuntoBien: #siguiendo las convenciones de python en clases la primera letra siempre es mayuscula

    #constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self):
        print('move')

    def draw(self):
        print('draw')


punto3 = PuntoBien(10, 20)
print(punto3.x)
#los atributos de la clase se pueden modificar de la siguiente manera
punto3.x = 30
print(punto3.x)
