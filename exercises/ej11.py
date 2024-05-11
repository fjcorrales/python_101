#Definir una clase 'Dado' que tenga un metodo llamado 'tirada' y que este devuelva una tupla de valores

import random
class Dado:

    def tirada(self):
        valor1 = random.randint(1, 6)
        valor2 = random.randint(1, 6)
        result = (valor1, valor2)
        print(result)


dado = Dado()
print(dado.tirada())
