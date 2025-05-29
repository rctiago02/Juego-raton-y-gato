# random para el queso y las barreras
# import random

def crear_tablero(filas, columnas, pos_raton, pos_gato):

    tablero = []


    for _ in range(filas):
        lista = [" • " for _ in range(columnas)]
        tablero.append(lista)

    tablero[pos_gato[0]][pos_gato[1]] = "🐱 "
    tablero[pos_raton[0]][pos_raton[1]] = "🐀 "
    

    if pos_raton == pos_gato:
        tablero[pos_raton[0]][pos_raton[1]] = "🐱 "
        
    return tablero

def imprimir_tablero(tablero):
    for fila in tablero:
        print(" ".join(fila))



