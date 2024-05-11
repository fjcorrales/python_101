#un paquete es un contenedor de diferentes modulos, básicamente una carpeta que creamos en el directorio del proyecto
#donde almacenamos nuestros modulos para no sobrepopular la carpeta principal del proyecto

#para este tema hemos creado una carpeta en el directorio llamada 'ecommerce' donde almacenaremos los modulos
#de una app de comercio electronico

#Para hacer que una carpeta sea un paquete necesitamos crear un fichero especifico el fichero '__init__.py'
#una vez creado el compilador de python tratara ese directorio como un paquete
#cuando ya tenemos esto creado, podemos ir llenando el paquete con modulos funcionales

#Hemos añadido la clase de envios y vamos a usarla en este documento
import ecommerce.envios
#de esta forma hemos importado el modulo de envios de dentro del paquete ecommerce

ecommerce.envios.calcular_envio()   #y así accedemos a la funcion de dentro del modulo dentro del paquete

#Sin embargo esto es un poco engorroso, por lo que se suele hacer uso de la forma de importacion con la sentencia 'from'
from ecommerce.envios import calcular_envio

calcular_envio() #y asi nos ahorramos tener que poner tanto punto

#con esta forma tambien podemos importar el modulo completo directamente
from ecommerce import envios

envios.calcular_envio() #y asi accederiamos a la funcion