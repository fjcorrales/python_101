#Conceptos basicos de listas

nombres = ['Jon', 'Bob', 'Sara', 'Miguel', 'Daniel']
#Cuando queremos acceder a un elemento de una lista podemos acceder mediante [] y un numero
print(nombres[0])
#esto no solo sirve para imprimir elementos si no tambien para modificarlos
#si queremos hacerlo en el orden inverso, basta con empezar desde -1 e ir subiendo
print(nombres[-1])
print(nombres[-2])

#Si queremos un rango de elementos usamos el operador ':' entre [] (OJO:esto siempre devuelve una lista nueva)
print(nombres[1:])
#si ponemos dos numeros en el : obtendremos un intervalo no cerrado (no se incluye el ultimo elemento)
print(nombres[1:3])
#si no pusieramos ningun numero obtendriamos toda la lista
print(nombres[:])