#Vamos a ver como trabajar con ficheros y directorios haciendo uso de la librería estandar de pathlib
#la docu se puede encontrar aqui https://docs.python.org/3/py-modindex.html
import pathlib
from pathlib import Path

#en informatica entendemos path como camino o direccion que es lo que nos indica la ruta de carpetas a seguir para encontrar
#un directorio o archivo. Podemos encontrar 2 tipos de rutas:
#Rutas absolutas: una ruta absoluta es la que va desde el origen del disco hasta el arcihvo/directorio deseado
#c:\Program Files\Microsoft (windows) /////\\\\\ /usr/local/bin (mac)
#Rutas relativas: una ruta relativa es una ruta que va desde una subcarpeta al archivo/directorio deseado
#pythonproject/ecommerce

x = Path()  #si no le ponemos ningun argumento de entrada, esto refernciara el directorio actual (notes)

print(x.exists())   #para saber si existe una ruta
#Path("emails").mkdir()  #crea directorios
#Path("emails").rmdir()  #elimina directorios
print(x.glob('*')) #nos permite buscar archivos en el directorio actual siguiendo el patron que se pase como valor '*' es para buscar todos
#esto nos devuelve un generator objecto sobre el que se puede iterar

for file in x.glob('*'):
    print(file)

