#Se usand cuando queremos guardar informacion como pares de "clave" asociadas a un "valor" (clave: valor)
#el diccionario se define con {}
#cada clave ha de ser unica y si repetimos una nos dara un error, las claves pueden ser strings o numeros
#los valores pueden repetirse y ser cualquier cosa
cliente = {
    "nombre": "Juan Perez",
    "edad": "34",
    "es_valido": "True"
}

#ahora para acceder a cada elemento podemos usar [] y especificar la clave para obtener el valor
print(cliente["nombre"])
#si ponemos una clave que no exista, nos dara un error
#print(cliente["Nombre"])  #para hacer que funcione el resto de la prueba hay que comentar esta linea
#podemos apañar esto usando el metodo get
print(cliente.get("cumpleaños"))    #este nos devolvera "None" que es que no existe en vez de un error
#se le puede añadir un valor por defecto a la funcion get
print(cliente.get("cumpleaños", "24 de agosto"))

#los valores se pueden modificar como en una lista solo que en vez de poner entre [] el indice, pondremos la clave
#y podemos añadir pares simplemente haciendo una modificacion
cliente["cumpleaños"] = "24 de agosto"  #esto añade este par clave-valor al diccionario
print(cliente["cumpleaños"])

