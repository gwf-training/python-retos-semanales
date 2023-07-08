# Reto #12: VIERNES 13
#Publicación: 20/03/23 | FÁCIL

#Crea una función que sea capaz de detectar si existe un viernes 13 en el mes y el año indicados.
#- La función recibirá el mes y el año y retornará verdadero o falso.
from datetime import datetime
import random
import locale

# Setea la variable LC_ALL al conjunto de código UTF-8 con descripción español España
locale.setlocale(locale.LC_ALL,'es_ES.UTF-8')

def es_viernes_13(year: int, month: int) -> bool:
    d = datetime(year, month, 13)
    print(d.strftime("%A %d de %B de %Y"))
    #Weekday as a number 0-6, 0 is Sunday
    return d.strftime("%w") == "5"

if __name__ == '__main__':
    year = random.choice(range(0, 2023))
    month = random.choice(range(1, 13))
    print("Es viernes 13:", es_viernes_13(year, month))
