from typing import List, Tuple
import os
from readchar import readkey, key

def convertir_mapa_a_matriz(laberinto: str) -> List[List[str]]:
    return [list(fila) for fila in laberinto.split("\n")]

def mostrar_mapa(mapa: List[List[str]]):
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpiar la pantalla  con cls y clear
    for fila in mapa:
        print(''.join(fila))

def main_loop(mapa: List[List[str]], inicio: Tuple[int, int], fin: Tuple[int, int]):
    px, py = inicio
    mapa[px][py] = 'P'  # Colocamos al jugador en la posición inicial

    while (px, py) != fin:
        mostrar_mapa(mapa)
        print("Llegaste al Final : ", end='')

        movimiento = readkey()

        # Calculamos la  nueva posición basada en el movimiento
        nueva_px, nueva_py = px, py
        if movimiento == key.UP:
            nueva_px -= 1
        elif movimiento == key.DOWN:
            nueva_px += 1
        elif movimiento == key.LEFT:
            nueva_py -= 1
        elif movimiento == key.RIGHT:
            nueva_py += 1

        # Verificamos si la nueva posición es válida
        if 0 <= nueva_px < len(mapa) and 0 <= nueva_py < len(mapa[0]) and mapa[nueva_px][nueva_py] != '#':
            mapa[px][py] = '.'  # Restaurar la posición anterior
            px, py = nueva_px, nueva_py  # Actualizar la posición del jugador
            mapa[px][py] = 'P'  # Mover al jugador a la nueva posición

# laberinto
laberinto = """..###################
....#...............#
#.#.#####.#########.#
#.#...........#.#.#.#
#.#####.#.###.#.#.#.#
#...#.#.#.#.....#...#
#.#.#.#######.#.#####
#.#...#.....#.#...#.#
#####.#####.#.#.###.#
#.#.#.#.......#...#.#
#.#.#.#######.#####.#
#...#...#...#.#.#...#
###.#.#####.#.#.###.#
#.#...#.......#.....#
#.#.#.###.#.#.###.#.#
#...#.#...#.#.....#.#
###.#######.###.###.#
#.#.#.#.#.#...#.#...#
#.#.#.#.#.#.#.#.#.#.#
#.....#.....#.#.#.#.#
###################.."""


mapa = convertir_mapa_a_matriz(laberinto)
inicio = (0, 0)
fin = (len(mapa)-1, len(mapa[0])-1)

main_loop(mapa, inicio, fin)