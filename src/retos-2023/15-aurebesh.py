# Reto #15: AUREBESH
# Publicación: 10/04/23 | FÁCIL

#Crea una función que sea capaz de transformar Español al lenguaje básico del universo Star Wars: el "Aurebesh".
#- Puedes dejar sin transformar los caracteres que no existan en "Aurebesh".
#- También tiene que ser capaz de traducir en sentido contrario.
# 
#¡Que la fuerza os acompañe!

#IMPORTANTE: Ejecutar export PYTHONPATH=/Users/f12445/Personal/dev/cursos/python/mouredev/python-retos/src
#from modules.customstrings import get_letters

basic_aurebesh = {
        "a": "aurek", "b": "besh", "c": "cresh", "d": "dorn", "e": "esk", "f": "forn", "g": "grek", "h": "herf",
        "i": "isk", "j": "jenth", "k": "krill", "l": "leth", "m": "merm", "n": "nern", "o": "osk", "p": "peth", "q": "qek",
        "r": "resh", "s": "senth", "t": "trill", "u": "usk", "v": "vev", "w": "wesk", "x": "xesh", "y": "yirt", "z": "zerek",
        'ñ': 'ñ'}

def get_map_basic_to_aurebesh() -> dict:
    return basic_aurebesh

def get_map_aurebesh_to_basic() -> dict:
    aurebesh_basic = dict()
    for key, value in basic_aurebesh.items():
        aurebesh_basic[value] = key 
    return aurebesh_basic

def translate_to_aurebesh(text: str) -> str:
    letters = [*text.lower()]
    new_text = []
    for letter in letters:
        if basic_aurebesh.get(letter) is not None:
            new_text.append(basic_aurebesh[letter])
        else:
            new_text.append(letter)
    return "".join(new_text)

def translate_to_basic(text: str) -> str:
    new_text = str(text)
    for key, value in get_map_aurebesh_to_basic().items():
        new_text = new_text.replace(key, value)
    return new_text

if __name__ == '__main__':
    print('Reto #15: AUREBESH')
    palabra_basic = "¡Que la fuerza os acompañe!"
    palabra_aurebesh = translate_to_aurebesh(palabra_basic)
    print(f'{palabra_basic} -> {palabra_aurebesh}')
    result = translate_to_basic(palabra_aurebesh)
    print(f'{palabra_aurebesh} -> {result}')
