comando = ''
encendido = False
while True:
    comando = input('> ').lower()
    if comando == 'help':
        print('Lista de comandos: ')
        print('start - enciende el coche\n'
              'stop - para el coche\n'
              'quit - salir \n')
    elif comando == 'start':
        if not encendido:
            print('El coche esta en marcha\n')
            encendido = True
        else:
            print('El coche ya está encendido\n')
    elif comando == 'stop':
        if encendido:
            print('Se ha parado el coche\n')
            encendido = False
        else:
            print('El coche ya está parado\n')
    elif comando == 'quit':
        if encendido:
            print('No puede salir del coche en marcha\n')
        else:
            print('Saliendo del coche')
            break
    else:
        print('Comando introducido no reconocido, escriba "help" para conocer los comandos disponibles')