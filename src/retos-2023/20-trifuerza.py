### Reto #20: LA TRIFUERZA
#### Publicación: 15/05/23 | MEDIA
#
#¡El nuevo "The Legend of Zelda: Tears of the Kingdom" ya está disponible! 
#Crea un programa que dibuje una Trifuerza de "Zelda"
#formada por asteriscos.
#- Debes indicarle el número de filas de los triángulos con un entero positivo (n).
#- Cada triángulo calculará su fila mayor utilizando la fórmula 2n-1.
#Ejemplo: Trifuerza 2
#
#    *
#   ***
#  *   *
# *** ***

def print_trifuerza(nivel: int) -> None:
    for i in range(1, nivel + 1):
        desplazamiento = "  " * (nivel-i)
        print(f'{desplazamiento}{" *  " * i}')
        print(f'{desplazamiento}{"*** " * i}')

if __name__ == '__main__':
    print('Reto #20: LA TRIFUERZA')
    print('Publicación: 15/05/23 | MEDIA\n')
    print_trifuerza(6)