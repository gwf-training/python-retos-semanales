# Reto #13: ADIVINA LA PALABRA
# Publicación: 27/03/23 | FÁCIL

#Crea un pequeño juego que consista en adivinar palabras en un número máximo de intentos:
#- El juego comienza proponiendo una palabra aleatoria incompleta
#  - Por ejemplo "m_ur_d_v", y el número de intentos que le quedan
#- El usuario puede introducir únicamente una letra o una palabra (de la misma longitud que
#  la palabra a adivinar)
#  - Si escribe una letra y acierta, se muestra esa letra en la palabra. Si falla, se resta
#    uno al número de intentos
#  - Si escribe una resolución y acierta, finaliza el juego, en caso contrario, se resta uno
#    al número de intentos
#  - Si el contador de intentos llega a 0, el jugador pierde
#- La palabra debe ocultar de forma aleatoria letras, y nunca puede comenzar
#  ocultando más del 60%
#- Puedes utilizar las palabras que quieras y el número de intentos que consideres


import random
import string
import re

MAXIMO_INTENTOS_FALLIDOS = 3
MASCARA = "*"
ALFABETO = set(string.ascii_uppercase)
#VOCALES = set({"A","E","I","O","U"})
#CONSONANTES = ALFABETO - VOCALES

PALABRAS = ['TRANSUSTANCIACION', 'ARTERIOSCLEROSIS', 'MURCIELAGO', 'DESOXIRRIBONUCLEICO', 'ARGENTINA', 'CHICHARRA']
        

def input_random_letter(palabra_enmascarada: str) -> str:
    letter = random.choice(list(ALFABETO))
    print(f'Letra (A-Z)?: \t{letter}')
    if letter not in palabra_enmascarada:
        return letter
    else:
        print('Caramba, la letra ya fue seleccionada\n')
        return input_random_letter(palabra_enmascarada)
    
def input_manual_letter(palabra_enmascarada: str) -> str:
    letter = input(f'Letra (A-Z)?: \t').upper()
    if len(letter) == 1 and letter not in palabra_enmascarada:
        return letter
    else:
        print('Caramba, la letra ya fue seleccionada \n')
        return input_manual_letter(palabra_enmascarada)

def enmascarar_palabra(palabra: str) -> list[str]:
    letras = set(re.findall(r'[A-Z]', palabra))
    cantidad_letras_enmascaradas = int(len(letras) * 0.6) + 1
    letras_enmascaradas = set()
    for _ in range(cantidad_letras_enmascaradas):
        letra = random.choice(list(letras))
        letras_enmascaradas.add(letra)
        letras.remove(letra)
    palabra_enmascarada = palabra
    for letra in letras_enmascaradas:
        palabra_enmascarada = palabra_enmascarada.replace(letra, MASCARA)
    return palabra_enmascarada

def seleccionar_palabra() -> tuple:
    palabra_original = random.choice(PALABRAS)
    palabra_enmascarada = enmascarar_palabra(palabra_original)
    return (palabra_original, palabra_enmascarada)

def verficar_letra(letra: str, palabra_original: str, palabra_enmascarada: str) -> tuple:
    if letra in palabra_original:
        new_palabra_enmascarada = list(palabra_enmascarada)
        for found in re.finditer(letra, palabra_original):
            index, _ = found.span()
            new_palabra_enmascarada[index] = letra
        return (True, "".join(new_palabra_enmascarada))
    else:
        return (False, palabra_enmascarada)

def verificar_palabra(dato, palabra_original, palabra_enmascarada) -> tuple:
    if dato == palabra_original:
        return True, palabra_original
    else:
        return False, palabra_enmascarada
    
def jugar():
    print("-----------------------------------------------------------------------------")
    palabra_original, palabra_enmascarada = seleccionar_palabra()
    intentos_fallidos = 0
    adivino_palabra = False
    letras_ingresadas = []
    total_letras = len(palabra_original)
    while not adivino_palabra and intentos_fallidos < MAXIMO_INTENTOS_FALLIDOS:
        cantidad_letras_enmascaradas = len(list(filter(lambda l: l == '*' , palabra_enmascarada)))
        print(f'\nPALABRA ({total_letras-cantidad_letras_enmascaradas}/{total_letras}):\t{palabra_enmascarada}\t ingresos: {list(letras_ingresadas)}')
        #dato = input_random_letter(palabra_enmascarada)
        dato = input_manual_letter(palabra_enmascarada)
        if len(dato) == 1:
            letras_ingresadas.append(dato)
            adivino, palabra_enmascarada = verficar_letra(dato, palabra_original, palabra_enmascarada)
        else:
            adivino, palabra_enmascarada = verificar_palabra(dato, palabra_original, palabra_enmascarada)

        if adivino:
            if palabra_original == palabra_enmascarada:
               adivino_palabra = True
            else:
                print("bien!!!")
        else:
            intentos_fallidos += 1
            if intentos_fallidos < MAXIMO_INTENTOS_FALLIDOS:
                print(f'Te quedan {MAXIMO_INTENTOS_FALLIDOS - intentos_fallidos} intentos\n')

    if adivino_palabra:
        print(f"\nFelicitaciones!!! has adivinado la palabra es {palabra_original}!")
    else:
        print(f"\nLo siento la palabra es {palabra_original}, la proxima será!")

if __name__ == '__main__':
    jugar()