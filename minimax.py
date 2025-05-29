from variables import posicion_gato, posicion_raton

def movimientos_validos(pos):
    """Devuelve los movimientos posibles desde una posición"""
    movs = []
    fila, col = pos
    # o fila = pos[0] y col = pos[1]
    
    # vemos si los movimientos son permitidos dentro del tablero
    if fila > 0:
        movs.append((fila-1, col))    
    if fila < 4:
        movs.append((fila+1, col))
    if col > 0:
        movs.append((fila, col-1))
    if col < 4:
        movs.append((fila, col+1))
    return movs

def evaluar(gato, raton):
    if gato == raton:
        return 100
    
    # Manhattan. estudiar (necesario?), euclidiana (estudiar),
    # calcula la distancia de un animalito a otro y lo retorna en negativo para que no se una preferencia para movimiento del gato
    distancia = abs(gato[0]-raton[0]) + abs(gato[1]-raton[1])
    return -distancia




def minimax(gato, raton, profundidad, es_turno_gato):
    # Si el gato esta en el mismo lugar que raton, o la profundidad es 0. Termina la recursividad
    if gato == raton or profundidad == 0:
        # Se llama a la funcion evaluar
        return evaluar(gato, raton)
    


    # cuando juega gato maximizamos puntaje
    if es_turno_gato:
        mejor_valor = float("-inf")

        # Mientras el movimientos de gato exista en movimientos_validos, comienza...
        for mov in movimientos_validos(gato):
            # llama a la funcion minimax y comienza una recursividad. guardamos el valor que se encontro
            valor = minimax(mov, raton, profundidad-1, False)

            #
            # Si valor es mejor que el mejor_valor guardado, variable mejor_valor actualiza a valor
            #
            
            if valor > mejor_valor:
                mejor_valor = valor
        return mejor_valor
    
    # cuadno juega raton minimizamos el puntaje

    else:
        mejor_valor = float("inf")
        for mov in movimientos_validos(raton):
            valor = minimax(gato, mov, profundidad-1, True)
            if valor < mejor_valor:
                mejor_valor = valor
        return mejor_valor


#def minimax(gato, raton, profundidad, es_turno_gato):
    valor = float("-inf")

    for mov in movimientos_validos():
        valor = minimax(gato, raton, profundidad-1, es_turno_gato)
        if valor > mejor_valor:
            mejor_valor = valor
        return mejor_valor
    
    for mov in movimientos_validos():
        valor = minimax(gato, raton, profundidad-1, False)
        if valor < mejor_valor:
            mejor_valor = valor
        return mejor_valor

    
        



# Esta funcion es la que encuentra el mejor movimiento para el gato
def mejor_movimiento_gato():
    mejor_valor = float("-inf")
    mejor_mov = None # None = Nada

    for mov in movimientos_validos(posicion_gato):
        # Evaluamos el movimiento con profundidad 3 (gato-ratón-gato-ratón)
        valor = minimax(mov, posicion_raton, 3, False)

        #
        # Si valor es mayor que mejor_valor guardado(mirar mas arriba), actualizar el MEJOR_MOV 
        #

        if valor > mejor_valor:
            mejor_valor = valor
            mejor_mov = mov
    
    # retonra mejor_mov
    return mejor_mov