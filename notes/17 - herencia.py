class Perro:
    def camina(self):
        print('Camina')


class Gato:
    def camina(self):
        print('Camina')


#Esto esta mal, ya que ambos animales cuentan con la misma funcion
#esto puede provocar que si en algun momento hemos cometido algun error al programar
#la funcion tendremos que hacer una modificacion sobre amnbos, esto a mayor escala es un problema muy grave
#debido a temas de trazabilidad

#La herencia lo que nos permite es hacer que una clase sea "hija" de otra haciendo asi que compartan un mismo
#set de funciones

class Mamifero:
    def camina(self):
        print('Camina')


#Hemos creado una clase padre llamada mamifero ahora tenemos que hacer que perro y gato hereden de esta
#para realizar la herencia basta con que a la hora de definir una clase le pongamos entre parentesis la
#clase padre. Aunque haya herencia, podemos seguir definiendo funciones dentro de estas clases para hacer mas
#especifica una clase

class Perro2(Mamifero):
    pass    #a python no le mola que haya clases vacias por lo que la siguiente linea a la definicion de la clase
            #dara error, por lo que para evitar esto podemos usar la sentencia pass


class Gato2(Mamifero):
    def maullar(self):
        print('miau')


perro = Perro2()
perro.camina()  #esto realiza la funcion de camina() definida dentro de mamifero dada la herencia

gato = Gato2()
gato.camina()   #esto realiza la funcion de camina() definida dentro de mamifero dada la herencia
gato.maullar()  #ejecutamos la funcion maullar() propia de la clase gato