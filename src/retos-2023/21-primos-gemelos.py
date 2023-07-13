### Reto #21: NÚMEROS PRIMOS GEMELOS
#### Publicación: 22/05/23 | MEDIA
#
#Crea un programa que encuentre y muestre todos los pares de números primos gemelos en un rango concreto.
#El programa recibirá el rango máximo como número entero positivo.
#
#- Un par de números primos se considera gemelo si la diferencia entre ellos es exactamente 2. Por ejemplo (3, 5), (11, 13)
#- Ejemplo: Rango 14 -> (3, 5), (5, 7), (11, 13)

def es_primo(number: int) -> bool:
    if number == 1 or number == 0: return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def primos_gemelo(number: int) -> list[tuple]:
    result = list()
    primo_anterior = 2
    for n in range(3, number + 1):
        if es_primo(n):
            if n - primo_anterior == 2:
                result.append((primo_anterior, n))
            primo_anterior = n
    return result

if __name__ == '__main__':
    print('Reto #21: NÚMEROS PRIMOS GEMELOS')
    print('Publicación: 22/05/23 | MEDIA')
    print(primos_gemelo(5))
    print(primos_gemelo(14))
    print(primos_gemelo(50))
