# Reto #27: CUENTA ATRÁS
# Publicación: 03/07/23 | MEDIA
#
#Crea una función que reciba dos parámetros para crear una cuenta atrás.
#- El primero, representa el número en el que comienza la cuenta.
#- El segundo, los segundos que tienen que transcurrir entre cada cuenta.
#- Sólo se aceptan números enteros positivos.
#- El programa finaliza al llegar a cero.
#- Debes imprimir cada número de la cuenta atrás.

import time

def countdown(start: int, sleep: int):
    if start < 0: raise ValueError('Invalid start, must be positive')
    if sleep < 0: raise ValueError('Invalid sleep, must be positive')
    for step in reversed(range(start+1)):
        time.sleep(sleep)        
        print(step)

if __name__ == '__main__':
    print('Reto #27: CUENTA ATRÁS')
    print('Publicación: 03/07/23 | MEDIA')
    countdown(10, 1)