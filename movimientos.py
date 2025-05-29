from variables import filas, columnas, posicion_gato, posicion_raton, turno_raton
from minimax import mejor_movimiento_gato

# Esta función permite que el jugador (gato o ratón) haga un movimiento válido dentro del tablero.
def definir_movimiento():
    


    while True:  # Repite hasta que el movimiento sea válido
        global posicion_gato, posicion_raton, turno_raton  # Se usan estas variables globales para actualizar las posiciones directamente
        


        # Se determina quién juega: si es el turno del ratón, se usa su posición; si no, la del gato
        jugador = posicion_raton if turno_raton else posicion_gato
        print(f"Turno del {'raton' if turno_raton else 'gato'}")  # Muestra en pantalla quién debe moverse



        """
        La funcion tiene que pedir al usuario que ingresar si el raton juega contra la npc o contra otro usuario


        """

#######
        if not turno_raton:
            movimiento = mejor_movimiento_gato()
            posicion_gato[:] = list(movimiento)
            turno_raton = not turno_raton
            break


        
        # Se pide al usuario que elija una dirección con las teclas w, s, a, d
        movimiento = input("muevete con: w, s, a, d").lower()
        
        # Si el movimiento no es válido, se vuelve a pedir
        if movimiento not in ["w", "s", "a", "d"]:
            continue

        # Se hace una copia de la posición actual para calcular el nuevo movimiento
        nueva_posicion = jugador.copy()

        # Se ajusta la posición dependiendo de la dirección elegida
        if movimiento == "w":
            nueva_posicion[0] -= 1  # Arriba: disminuye la fila
        elif movimiento == "s":
            nueva_posicion[0] += 1  # Abajo: aumenta la fila
        elif movimiento == "a":
            nueva_posicion[1] -= 1  # Izquierda: disminuye la columna
        elif movimiento == "d":
            nueva_posicion[1] += 1  # Derecha: aumenta la columna
        
        # Se verifica que la nueva posición esté dentro de los límites del tablero
        if (0 <= nueva_posicion[0] < filas) and (0 <= nueva_posicion[1] < columnas):


            #######
            posicion_raton[:] = nueva_posicion
            #######
            
            # Cambia el turno para que juegue el otro
            turno_raton = not turno_raton
            break  # Sale del ciclo porque el movimiento fue válido
        else:
            # Si la nueva posición es inválida (fuera del tablero), lo indica y repite
            print("movimiento invalido")
