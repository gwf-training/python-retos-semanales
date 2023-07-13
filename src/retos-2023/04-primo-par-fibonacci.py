#Reto #4: PRIMO, FIBONACCI Y PAR
#Publicación: 23/01/23 | MEDIA

#Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
#Ejemplos:
#- Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
#- Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
import math

def es_par(number: int) -> bool:
    return number % 2 == 0

def es_primo(number: int) -> bool:
    if number == 1 or number == 0: return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def es_cuadrado_perfecto(number):
    sqrt = int(math.sqrt(number))
    return sqrt * sqrt == number

def es_fibonacci(number: int) -> bool:
    if number < 0: return False
    return es_cuadrado_perfecto(5*number*number+4) or es_cuadrado_perfecto(5*number*number-4)


def process(number: int):
    msg_par = "es par" if es_par(number) else "es impar"
    msg_primo = "es primo" if es_primo(number) else "no es primo"
    msg_fibonacci = "es fibonacci" if es_fibonacci(number) else "no es fibonacci"
    result = f'{number} {msg_primo}, {msg_fibonacci} y {msg_par}'
    print(result)

process(0)
process(1)
process(2)
process(5)
process(7)
process(8)
process(10)

