def dic():
    '''un equipo fútbol tiene 6 jugadores cada uno de estos jugadores se caracteriza por tener las
    siguientes características: cedula, nombre, apellido velocidad, aceleración, potencia en el
    disparo; se desea un programa que registre estos 6, calcule el jugador más rápido por, el
    promedio de velocidad de todos los jugadores, el jugador com mejor potencia y el jugador con
    mayor aceleración de todos los equipos.
        '''
    dicJugadores = {'jugador1': {'cedula': '123456789', 'nombre': 'jose', 'apellido': 'perez',
                                 'velocidad': 10, 'aceleracion': 14, 'potencia': 19},
                    'jugador2': {'cedula': '987654321', 'nombre': 'manolo', 'apellido': 'lopez',
                                 'velocidad': 19, 'aceleracion': 8, 'potencia': 13},
                    'jugador3': {'cedula': '159753456', 'nombre': 'anacleta', 'apellido': 'gaviria',
                                 'velocidad': 5, 'aceleracion': 18, 'potencia': 15},
                    'jugador4': {'cedula': '987654159', 'nombre': 'arnold', 'apellido': 'jabon',
                                 'velocidad': 17, 'aceleracion': 11, 'potencia': 10},
                    'jugador5': {'cedula': '123123123', 'nombre': 'fifi', 'apellido': 'potasio',
                                 'velocidad': 7, 'aceleracion': 19, 'potencia': 11},
                    'jugador6': {'cedula': '456456456', 'nombre': 'maria', 'apellido': 'jertrudiz',
                                 'velocidad': 4, 'aceleracion': 12, 'potencia': 20}, }

    def jugadorMasRapido(dicJugadores, aux=0, jugador=''):
        for key, value in dicJugadores.items():
            if value['velocidad'] > aux:
                aux = value['velocidad']
                jugador = key
        return print('El jugador mas rápido es el {0} con velocidad {1}'.format(jugador, aux))

    def promedioVelocidad(dicJugadores, aux=0, contador=0):
        for key, value in dicJugadores.items():
            aux += value['velocidad']
            contador = contador + 1
        aux = aux / contador
        return print('El promedio de velocidad de todos los jugadores es de {}'.format(aux))

    # jugadorMasRapido(dicJugadores)
    # promedioVelocidad(dicJugadores)

    '''un almacén de deporte tiene una producción de 6 patinetas cada una de estas se caracteriza por: 
    Tipo material, velocidad, ancho, alto, color, precio. Se desea realizar un programa que almacene 
    las 15 patinetas. Y que me permita saber el costo total de las patinetas, la segunda patineta con 
    mejor velocidad.'''

    dicPatinetas = {'patineta1': {'material': '123456789', 'velocidad': 18, 'ancho': 10,
                                  'alto': 10, 'color': 14, 'precio': 19},
                    'patineta2': {'material': '987654321', 'velocidad': 21, 'ancho': 4,
                                  'alto': 19, 'color': 8, 'precio': 13},
                    'patineta3': {'material': '159753456', 'velocidad': 13, 'ancho': 8,
                                  'alto': 5, 'color': 18, 'precio': 15},
                    'patineta4': {'material': '987654159', 'velocidad': 158, 'ancho': 9,
                                  'alto': 17, 'color': 11, 'precio': 10},
                    'patineta5': {'material': '123123123', 'velocidad': 61, 'ancho': 7,
                                  'alto': 7, 'color': 19, 'precio': 11},
                    'patineta6': {'material': '456456456', 'velocidad': 48, 'ancho': 11,
                                  'alto': 4, 'color': 12, 'precio': 20}, }

    def sdaPatMasRapida(dicPatinetas, aux=0, sdaPat=0, patineta=''):
        for key, value in dicPatinetas.items():
            if value['velocidad'] > aux:
                aux = value['velocidad']

        for key2, value2 in dicPatinetas.items():
            if value2['velocidad'] != aux and value2['velocidad'] > sdaPat:
                sdaPat = value2['velocidad']
                patineta = key2

        return print('La segunda patineta más rápida es la {0} con velocidad {1}'.format(patineta, sdaPat))

    def costoTotalPat(dicPatinetas, aux=0):
        for key, value in dicPatinetas.items():
            aux += value['precio']
        return print('El costo total de todas las patinetas es de {}'.format(aux))

    # sdaPatMasRapida(dicPatinetas)
    # costoTotalPat(dicPatinetas)

    '''Escribir un programa que, pida el mes de nacimiento de 10 personas e imprima por pantalla el signo zodiacal 
       de una persona específica, el signo zodiacal más común (el que más se repite).'''

    dicPersonas = {'persona1': {'mes': 4}, 'persona2': {'mes': 5}, 'persona3': {'mes': 5}, 'persona4': {'mes': 5},
                   'persona5': {'mes': 6}, 'persona6': {'mes': 7}, 'persona7': {'mes': 4}, 'persona8': {'mes': 8},
                   'persona9': {'mes': 9}, 'persona10': {'mes': 1}}
    dicPersonas.update({'persona1': {'mes': 4}})
    dicZodiaco = {'aries': 4, 'tauro': 5, 'geminis': 6, 'cancer': 7, 'leo': 8, 'virgo': 9, 'libra': 10, 'escorpio': 11,
                  'sagitario': 12, 'capricornio': 1, 'acuario': 2, 'piscis': 3}

    def asignarMes(persona, mes):
        persona = '{}'.format(persona)
        if persona in dicPersonas:
            dicPersonas.update({persona: {'mes': mes}})
            return print(dicPersonas)

    def get_key(val):
        for key, value in dicZodiaco.items():
            if val == value:
                return key
        return "No existe ese mes"

    menuZodiaco = "----------Astrología----------\n"
    menuZodiaco += "Escribe un número en base a la acción que desees realizar\n"
    menuZodiaco += "1. Registrar meses de nacimiento\n"
    menuZodiaco += "2. Mostrar signo zodiacal de alguien en específico\n"
    menuZodiaco += "3. Signo zodiacal más común entre las personas registradas\n"
    menuZodiaco += "4. Mostrar personas \n"
    menuZodiaco += "5. Salir\n"
    cod = 0

    def punto4(cod, menuZodiaco):
        while(cod!=5):
            cod=int(input(menuZodiaco))

            if cod == 1:
                for i in range(len(dicPersonas.items())):
                    persona = input("Ingresa a cuál persona le asignarás la fecha de nacimiento: \n")
                    mes = int(input("Ingresa el número del mes de nacimiento: \n"))
                    asignarMes(persona, mes)
                    salir = input("Deseas asignar más fechas? (si) (no) \n")
                    if salir == 'no':
                        print()
                        break

            if cod == 2:
                persona = input("Ingresa la persona a la que se desea ver su signo zodiacal \n")
                persona = '{}'.format(persona)
                mes = dicPersonas[persona]['mes']
                print("La {0} tiene de signo {1}".format(persona, get_key(mes)))

            if cod == 3:
                vals = list(dicPersonas.values()) # Lista todos los valores de las llaves del diccionario
                maximo = max(vals, key=vals.count) # Halla el valor más frecuente
                signo = get_key(maximo['mes']) # De este valor más frecuente, se obtiene su subvalor
                print("El Signo más frecuente es {}".format(signo))

            if cod == 4:
                print(dicPersonas)

        print("Saliste del sistema, vuelve pronto! \n")

    # punto4(cod, menuZodiaco)

dic()
