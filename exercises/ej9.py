#Escribe un programa para encontrar el numero mas grande de una lista

numeros = [4, 2, 7, 8, 1, 0, 4]
mayor = 0

for num in numeros:
    if mayor < num:
        mayor = num

print(f'El número más grande de la lista es {mayor}')