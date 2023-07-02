
### Reto #3: EL GENERADOR DE CONTRASEÑAS
#### Publicación: 16/01/23 | MEDIA

#Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
#Podrás configurar generar contraseñas con los siguientes parámetros:
#- Longitud: Entre 8 y 16.
#- Con o sin letras mayúsculas.
#- Con o sin números.
#- Con o sin símbolos.
#(Pudiendo combinar todos estos parámetros entre ellos)

import random

LONG_MIN = 8
LONG_MAX = 16

# Fuente: https://www.ascii-code.com
def get_characters(include_uppercase:bool=False, include_numbers:bool=False, include_symbols:bool=False) -> list:
    characters = list(range(97, 123))
    if include_uppercase:
        characters += list(range(65, 91))
    if include_numbers:
        characters += list(range(48, 58))
    if include_symbols:
        characters += list(range(33, 48)) + list(range(58, 65)) + list(range(91, 97))
    return characters

def password_generator(size:int=LONG_MIN, include_uppercase:bool=False, include_numbers:bool=False, include_symbols:bool=False) -> str :
    size_validated = LONG_MIN if size < LONG_MIN else LONG_MAX if size > LONG_MAX else size
    characters = get_characters(include_uppercase, include_numbers, include_symbols)
    password = ""
    for _ in range(1, size_validated):
        password += chr(random.choice(characters))
    return password

print("password:", password_generator())
print("password:", password_generator(size=16))
print("password:", password_generator(size=16, include_uppercase=True))
print("password:", password_generator(size=16, include_uppercase=True, include_numbers=True))
print("password:", password_generator(size=16, include_uppercase=True, include_numbers=True, include_symbols=True))
print("password:", password_generator(size=16, include_numbers=True))
print("password:", password_generator(size=16, include_symbols=True))
print("password:", password_generator(size=-7)) #minimo default 8
print("password:", password_generator(size=13333)) #maximo default 8
