
### Reto #16: LA ESCALERA
#### Publicación: 17/04/23 | MEDIA

#Crea una función que dibuje una escalera según su número de escalones.
#- Si el número es positivo, será ascendente de izquiera a derecha.
#- Si el número es negativo, será descendente de izquiera a derecha.
#- Si el número es cero, se dibujarán dos guiones bajos(__).

#Ejemplo: 4
#        _
#      _|
#    _|
#  _|
#_|

def print_step_up(level: int):
    print(f'{"  " * level}_')
    for i in reversed(range(level)):
        print(f'{"  " * i}_|')

def print_step_down(level: int):
    print(f'_')
    for i in range(abs(level)):
        print(f' {"  " * i}|_')

def print_level_0():
    print("__")

def print_stair(level: int):
    fn = print_step_up if level > 0 else print_step_down if level < 0 else print_level_0
    fn()

if __name__ == "__main__":
    print("Reto #16: LA ESCALERA")
    print_stair(3)
    print_stair(0)
    print_stair(-3)
