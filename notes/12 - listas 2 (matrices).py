matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

#para acceder a una matrix hemos de pasar dos valores, una coordenada
print(matriz[0][0]) #nos tiene que dar el 1
print(matriz[1][1]) #nos tiene que dar el 5
print('\n')

#Tambien podemos utilizar bucles anidados para iterar sobre los elementos de la matriz
for fila in matriz:
    for elemento in fila:
        print(elemento)

#Las listas cuentan con muchos metodos que nos pueden facilitar realizar ciertas operaciones
#para esto es buena idea buscar en internet cuales hay y que nos permite hacer cada uno