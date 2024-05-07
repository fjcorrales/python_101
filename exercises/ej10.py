#Define un tipo llamado 'persona', ha de tener un atributo nombre y un metodo hablar

class Persona:

    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(f'habla {self.nombre}')   #aqui podemos ver el uso del parametro 'self' esto nos permite referenciar al mismo objeto


persona1 = Persona('Dani')
persona1.hablar()
