# Reto #14: OCTAL Y HEXADECIMAL
# Publicación: 03/04/23 | FÁCIL

#Crea una función que reciba un número decimal y lo trasforme a Octal y Hexadecimal.
#- No está permitido usar funciones propias del lenguaje de programación que realicen esas operaciones directamente.

import random
from enum import Enum

class HexadecimalChar(Enum):
    A = 10
    B = 11
    C = 12
    D = 13
    E = 14
    F = 15


def octal(number: int) -> str:
    cociente = number // 8
    resto = str(number % 8)
    if cociente == 0:
        return resto
    elif cociente < 8:
        return str(cociente) + resto
    else:
        return octal(cociente) + resto

def hexadecimal(number: int) -> str:
    cociente = number // 16
    resto = number % 16
    resto = str(resto) if resto <= 10 else HexadecimalChar(resto).name
    if cociente == 0:
        return resto
    elif cociente < 16:
        return str(cociente) + resto
    else:
        return hexadecimal(cociente) + resto

if __name__ == '__main__':

    numbers = [0,1,7,8,10, 15,16]
    for number in numbers:
        print(f"number: {number} \toctal: {octal(number)} \thexadecimal: {hexadecimal(number)}")

    for _ in range(10):
        number = random.choice(range(10000))
        print(f"number: {number} \toctal: {octal(number)} \thexadecimal: {hexadecimal(number)}")
