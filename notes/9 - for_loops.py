###el bucle for itera sobre items de una coleccion, se usa sobretodo con strings
# es decir, el bucle for en python se ejecuta tantas veces como elementos tenga la coleccion que se usa como variable
# de bucle, esta vasiable se llama item en estos ejemplos pero de normal se puede poner cualquier nomnbre
# como si fuera una variable mas###

for item in 'Python':
    print(item)

print('\n')

### En python podemos definir una lista con []###
nombres = ['Juan', 'Daniel', 'Maria']
for item in nombres:
    print(item)

print('\n')

###Tambien se puede utilizar con numeros
# en estos casos si queremos que itere sobre un amplio rango de numeros no hace falta escribir todos
# tenemos a nuestra disposicion la funcion in range###

for numero in range(10):
    print(numero)

print('\n')

for numero in range(5, 10):   #para poner un intervalo
    print(numero)

print('\n')

for numero in range(5, 10, 2): #para poner un intervalo y que de saltos
    print(numero)