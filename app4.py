#Strings en python
#"""A en python podemos hacer uso tanto de "" como de '' para declarar un
# string sin embargo a veces es necesario hacer un uso específico.
#
# Por ejemplo, si queremos meter apostrofes en el string
# es obligataorio hacer uso de las comillas dobles"""#

#curso = 'Python's course' #Da error
curso = "Python's course" #es correcto

#"""Y en el caso contrario hemos de hacer lo mismo, si queremos usar comillas
# dobles como caracter en el string, hemos de usar las simples para
# definir el mismo"""#

#curso = "Python para "principiantes"" #Da error
curso = 'Python para "principiantes"'


#"""Existen tambien las comillas triples, estas se utilizan para cadenas
# de texto muy largas y que ocupan varias lineas, como por ejemplo las que conforman un correo
# Estas comillas triples pueden tanto ser simples como dobles y se aplica
# el concepto anterior"""#

curso = ''' 

Buenos dias, 

Llamamos para contactarle sobre el seguro de su coche.

Atentamente.
Unos pesaos
'''
print(curso)

#"""Tambien, podemos obtener un caracter en especifico de un string
# si hacemos uso de [] y un indice al hacer uso de la funcion print
# o cualquier otro metodo que haga referencia al string"""#

curso = 'Python para principiantes'
print(curso[0])
print(curso[-1])    #Se pueden usar indices negativos, con esto accedemos a los caracteres al final del string
print(curso[1:-1])  #Hay cosas más profundas con el operador :

#"""Existen un tipo de strings formateados, los cuales sirven para
# insertar variables dentro de strings sin necesidad de concatenarlos"""#
nombre = 'Daniel'
apellido = 'Corrales'
msg = f'{nombre} {apellido} es un informatico'
print(msg)

# Funciones con strings #
print(len(nombre))  #len() es como length() en java, obtiene la longitud del string o incluso de listas
print(nombre.upper())   #convierte todos los caracteres en matyusculas, crea una nueva variable, no modifica la existente
print(nombre.lower())   #igual que upper()
print(nombre.find('D')) #nos devuelve el indice de la primera aparicion del caracter entre '' en el string sobre el que se invoca (también funciona con palabras y obtenemos el indice donde empieza la palabra)
print(msg.replace('informatico', 'español'))    #cambia la primera instancia de la primera palabra que se le proporciona por la segunda, igual que upper crea un nuevo string temporal. Tambien funciona con letras

# operador 'in'
#""" esta es como un if, comprueba si hay algo en algun sitio y devuelve un boolean"""#

print('informatico' in msg)