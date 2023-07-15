
# Reto #25: EL CÓDIGO KONAMI
# Publicación: 19/06/23 | MEDIA

#Crea un programa que detecte cuando el famoso "Código Konami" se ha  introducido correctamente desde el teclado. 
#Si sucede esto, debe notificarse mostrando un mensaje en la terminal.

#codigo KONANI: Arriba, arriba, abajo, abajo, izquierda, derecha, izquierda, derecha, B, A, Start
#python -m pip install pynput
from pynput.keyboard import Key, KeyCode, Listener

KONAMI_CODE = [
    Key.up, Key.up, 
    Key.down, Key.down,
    Key.left, Key.right, 
    Key.left, Key.right,
    KeyCode.from_char("b"), KeyCode.from_char("a")
]

key_position: int = 0

def on_press(key):

    global key_position

    if key == Key.esc:
        print("Exit")
        return False    

    if key == KONAMI_CODE[key_position]:
        key_position += 1
    else:
        print('vuelve a intentar!!\n')
        key_position = 0

    if key_position == len(KONAMI_CODE):
        print("""
        \n
        ╦╔═╔═╗╔╗╔╔═╗╔╦╗╦  ╔═╗╔═╗╔╦╗╔═╗
        ╠╩╗║ ║║║║╠═╣║║║║  ║  ║ ║ ║║║╣ 
        ╩ ╩╚═╝╝╚╝╩ ╩╩ ╩╩  ╚═╝╚═╝═╩╝╚═╝
        \n
        """)
        return False

if __name__ == '__main__':
    print('Reto #25: EL CÓDIGO KONAMI')
    print('Publicación: 19/06/23 | MEDIA\n')

    with Listener(on_press=on_press) as listener:
        listener.join()