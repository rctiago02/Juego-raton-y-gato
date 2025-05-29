from tablero import crear_tablero, imprimir_tablero
from movimientos import definir_movimiento
from variables import filas, columnas, posicion_gato, posicion_raton, cont_mov
import os


# Crear 

while cont_mov > 0:
    cont_mov -= 1
    tablero = crear_tablero(filas, columnas, posicion_raton, posicion_gato)
    os.system('cls' if os.name == 'nt' else 'clear')
    imprimir_tablero(tablero)
    definir_movimiento()
    if posicion_raton == posicion_gato:
        tablero = crear_tablero(filas, columnas, posicion_raton, posicion_gato)
        imprimir_tablero(tablero)
        print("gato atrapo al raton")

        break


else:
    print("el raton escapo")


