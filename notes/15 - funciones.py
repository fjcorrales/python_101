#Conjutno de lineas de codigo encargadas de ejecutar codigo reutilizable
#usamos la palabra clave "def" y siempre que terminemos de definir la funcion
#añadiremos 2 espacios en blanco (esto son buenas practicas de formato)

def greet_user():
    print('Hola')
    print('Bienvenido\n')


greet_user()    #realizamos una llamada a la funcion para ejecutar los dos prints

#OJO es importante mencionar que python ejecuta linea por linea, por lo que si
#trartamos de hacer una llamada a la funcion antes de que hayamos definido esta
#nos dara un error pues no la va a encontrar, por lo que como buena practica
#hemos de definir siempre nuestras funciones al principio de nuestro codigo

#Asimismo a las funciones les podemos pasar parametros como por ejemplo a la funcion "print()"
#tambien podemos hacer que nuestras funciones reciban un parametro (o varios, se separan con ',').
def greet_user2(nombre):
    print(f'Hola {nombre}')
    print('Bienvenido\n')


greet_user2('Juan') #y esto podemos hacerlo con cualquier cosa que le pasemos
greet_user2('Perro')

#Si a una funcion que espera un parametro no le pasamos ninguna, nos dara un error.
#en otros lenguajes hemos de especificar que tipo de dato le estamos pasando
#ya sea un entero, una cadena... etc. En python no hace falta como hemos visto
#hay argumentos posicionales los cuales funcionan como esperamos, de forma especifica se usan en la funcion
#sin embargo hay argumentos clave donde si especificamos a que argumento hace referencia el orden no importara

def greet_user3(nombre, apellido):
    print(f'Hola {nombre} {apellido}')
    print('Bienvenido\n')


greet_user3('Daniel', 'Corrales')
greet_user3('Corrales', 'Daniel')   #estos no hacen uso de argumentos clave
greet_user3(apellido='Corrales', nombre='Daniel')  #Aqui hacemos uso del argumento clave donde especificamos, el orden deja de importar

#En las funciones podemos utilizar la sentencia de "return" para que esta funcion devuelva algo
#por defecto python devuelve 'none' es como si tuviera un 'return none'
def cuadrado(num):
    return num*num


print(f'El cuadrado de 2 es {cuadrado(2)}')
#el resultado de esta funcion lo podemos almacenar en una variable
var = cuadrado(3)
print(var)

#En las funciones tambien son importantes las excepciones, ya que nos permiten manejar errores
#y atraparlos para que no rompan la ejecucion del programa. Para esto hacemos uso de las sentencias
#'try' y 'except'
#podemos poner tantos 'except' como queramos para atrapar diferentes excepciones
try:
    edad = int(input('Edad: '))
    salario = 2000
    riesgo = salario / edad
    print(edad)
except ZeroDivisionError:
    print('La edad no puede ser 0') #Para que no nos salte la excepcion de division por 0 al calcular el riesgo
except ValueError:  #esto que ponemos aqui especifica que tipo de fallo queremos atrapar, 'ValueError' atrapa errores de conversion
    print('Valor no valido, ha de ser un valor numerico')
