#Reto #9: HETEROGRAMA, ISOGRAMA Y PANGRAMA
#Publicación: 27/02/23 | FACIL

#Crea 3 funciones, cada una encargada de detectar si una cadena de texto es un heterograma, un isograma o un pangrama.
#- Debes buscar la definición de cada uno de estos términos.

import string
import re

# Un heterograma (del griego héteros, 'diferente' y gramma, 'letra') es una palabra o frase que no 
# contiene ninguna letra repetida
def get_letters(phrase: str) -> list[str]:
    return re.findall(r'[a-z]', phrase.lower())

def get_unique_letters(phrase: str) -> list[str]:
    return list(set(get_letters(phrase)))

def es_heterograma(texto: str) -> bool:
    if len(texto) in (0,1): return False
    letters = get_unique_letters(texto)
    return len(texto) == len(letters)

#Un isograma (del griego isos, 'igual' y gramma, 'letra') es una palabra o frase en la que cada letra 
# aparece el mismo número de veces
def es_isograma(texto: str) -> bool:
    if len(texto) == 0: return False
    if len(texto) == 1: return True
    letters = get_letters(texto)
    letter_counters = dict.fromkeys(set(letters), 0)
    for letter in letters:
        letter_counters[letter] += 1
    letter_counters_sorted = sorted(letter_counters.items(), key=lambda x:x[1], reverse=True)
    return letter_counters_sorted[0][1] == letter_counters_sorted[-1][1] and letter_counters_sorted[0][1] != 1

#Un pangrama (del griego pan, 'todo' y gramma, 'letra') es una frase en la que aparecen todas las letras del abecedario. 
#Si cada letra aparece sólo una vez, formando por tanto un heterograma, se le llama pangrama perfecto.
def es_pangrama(texto: str) -> bool:
    alphabet = list(string.ascii_lowercase)
    letter_counters = dict.fromkeys(alphabet, 0)
    for letter in get_letters(texto):
        letter_counters[letter] += 1
    letter_counters_sorted = sorted(letter_counters.items(), key=lambda x:x[1])
    return letter_counters_sorted[0][1] != 0

if __name__ == '__main__':
    textos = ['centrifugado', 'murcielago','intestines', 'pepe', 'Benjamín pidió una bebida de kiwi y fresa. Noé, sin vergüenza, la más exquisita champaña del menú.']
    for texto in textos:
        print(f'Texto:\t"{texto}"')
        print(f'\tHeterograma: [{es_heterograma(texto)}], Isograma: [{es_isograma(texto)}], Pangrama: [{es_pangrama(texto)}]\n')