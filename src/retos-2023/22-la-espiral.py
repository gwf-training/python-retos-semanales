### Reto #22: LA ESPIRAL
#### Publicación: 29/05/23 | MEDIA
#
#Crea una función que dibuje una espiral como la del ejemplo.
#- Únicamente se indica de forma dinámica el tamaño del lado.
#- Símbolos permitidos: ═ ║ ╗ ╔ ╝ ╚
#Ejemplo espiral de lado 5 (5 filas y 5 columnas):
#════╗
#╔══╗║
#║╔╗║║
#║╚═╝║
#╚═══╝
#by mouredev

def print_espiral(size: int) -> None:
    for row in range(0, size):
        spiral = ""
        horizontal = row == 0
        for col in range(0, size):
            if row + col == size - 1:
                spiral += "╗" if col >= row else "╚"
                horizontal = col < row
            elif row - col == 1 and row < (size / 2):
                spiral += "╔"
                horizontal = True
            elif row == col and row >= (size / 2):
                spiral += "╝"
                horizontal = False
            else: 
                spiral += "═" if horizontal else "║"    
        print(spiral)

if __name__ == '__main__':
    print('Reto #22: LA ESPIRAL')
    print('Publicación: 29/05/23 | MEDIA')
    print_espiral(2)
    print_espiral(3)
    print_espiral(4)
    print_espiral(5)
    print_espiral(10)
    print_espiral(15)