import os
from readchar import readkey, key

def clear_and_print(number):
    """
    Borra la terminal y muestra el nuevo número.

    Args:
        number (int): El número a mostrar.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"Contador: {number}")

def main():
    """
    Función principal para ejecutar el bucle de lectura de la tecla 'n'.
    """
    contador = 0
    print(input("Por favor presione 'n' para incrementar el contador y para detener presione flecha 🡩 ")) 

    while True:
        k = readkey()

        if k == key.UP:
            print("Oh!! has presionado 🡩  para detener ")
            break

        elif k == 'n':
            contador += 1
            clear_and_print(contador)

            if contador == 50:
                print("Has llegado al número 50, el programa se detendrá.")
                break

if __name__ == "__main__":
    main()
