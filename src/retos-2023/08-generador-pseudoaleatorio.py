#Reto #8: EL GENERADOR PSEUDOALEATORIO
#MPublicación: 20/02/23 | MEDIA

#Crea un generador de números pseudoaleatorios entre 0 y 100.
#- No puedes usar ninguna función "random" (o semejante) del lenguaje de programación seleccionado.
import time

def random() -> int:
    return time.time_ns() % 101

if __name__ == '__main__':
    numero = random()
    print("numero aleatorio", numero)