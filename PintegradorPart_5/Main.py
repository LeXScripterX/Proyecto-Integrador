import os
import random
from typing import List, Tuple
from readchar import readkey, key

class Juego:
    # Constructor de la clase Juego.
    def __init__(self, mapa: List[List[str]], inicio: Tuple[int, int], fin: Tuple[int, int]):
        self.mapa = mapa
        self.inicio = inicio
        self.fin = fin
        self.posicion_actual = inicio
        
    # Muestra el mapa actual en la consola.
    def mostrar_mapa(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for fila in self.mapa:
            print(''.join(fila))

    # Contiene el bucle principal del juego para el movimiento del jugador.
    def main_loop(self):
        self.mapa[self.inicio[0]][self.inicio[1]] = 'P'
        # Bucle que se ejecuta hasta que el jugador alcanza la posición final.
        while self.posicion_actual != self.fin:
            self.mostrar_mapa()
            movimiento = readkey()
            self.mover_jugador(movimiento)
        print("¡Llegaste al final del laberinto!")

    def mover_jugador(self, movimiento: str):
        px, py = self.posicion_actual
        nueva_px, nueva_py = px, py

        if movimiento == key.UP:
            nueva_px -= 1
        elif movimiento == key.DOWN:
            nueva_px += 1
        elif movimiento == key.LEFT:
            nueva_py -= 1
        elif movimiento == key.RIGHT:
            nueva_py += 1
        
        # Actualiza la posición del jugador si el movimiento es válido.
        if 0 <= nueva_px < len(self.mapa) and 0 <= nueva_py < len(self.mapa[0]) and self.mapa[nueva_px][nueva_py] != '#':
            self.mapa[px][py] = '.'
            self.posicion_actual = (nueva_px, nueva_py)
            self.mapa[nueva_px][nueva_py] = 'P'

def cargar_mapa(path_a_mapas: str) -> Tuple[List[List[str]], Tuple[int, int], Tuple[int, int]]:
    archivos = os.listdir(path_a_mapas)
    archivo_mapa = os.path.join(path_a_mapas, random.choice(archivos))
    with open(archivo_mapa, 'r') as file:
        lineas = file.readlines()
        
    # Verifica que la primera línea tenga al menos 6 elementos.
    if len(lineas) == 0 or len(lineas[0].strip().split()) < 4:
        raise ValueError(f"El archivo {archivo_mapa} no tiene el formato esperado.")

    coords = lineas[0].strip().split()
    try:
        inicio = (int(coords[0]), int(coords[1]))
        fin = (int(coords[2]), int(coords[3]))
    except ValueError:
        raise ValueError(f"Las coordenadas en el archivo {archivo_mapa} no son válidas.")

    laberinto = ''.join(lineas[1:]).strip()
    if not laberinto:
        raise ValueError(f"El archivo {archivo_mapa} no contiene un laberinto válido.")

    mapa = [list(fila) for fila in laberinto.split("\n")]
    return mapa, inicio, fin

def main():
    path_a_mapas = "/home/iteza/Documentos/.GIT/Proyecto-Integrador/PintegradorPart_5/mapas/"
    try:
        mapa, inicio, fin = cargar_mapa(path_a_mapas)
        juego = Juego(mapa, inicio, fin)
        juego.main_loop()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()