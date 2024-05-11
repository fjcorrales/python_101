#un modulo no es mas que un archivo con codigo python que importamos a otro fichero para poder usar sus funciones o clases
#en este caso hemos creado un fichero llamado conversores en el que tenemos dos funciones, vamos a importarlo y a hacer
#uso de las mismas. Crear un modulo no es mas que crear un fichero, llenarlo de funciones e importatlo donde sea necesario

#para importar hacemos uso de la sentencia "import" esto hace que la clase que importamos se convierta en un objeto
import conversores

print(conversores.kg_to_lbs(80))
print(conversores.lbs_to_kg(177))

#no existe solo esta forma de realizar importaciones de modulos
#haciendo de uso de la sentencia "from" podemos importar una unica funcion a nuestro fichero
from conversores import kg_to_lbs, lbs_to_kg    #tambien podemos importar varias funciones de una usando la ','
print(kg_to_lbs(100))
print(lbs_to_kg(222))