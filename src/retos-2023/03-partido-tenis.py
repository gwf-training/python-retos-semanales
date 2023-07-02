
### Reto #3: EL PARTIDO DE TENIS
#### Publicación: 09/01/23 | MEDIA

#Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
#El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien gane cada punto del juego.
 
#- Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
#- Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
#  15 - Love
#  30 - Love
#  30 - 15
#  30 - 30
#  40 - 30
#  Deuce
#  Ventaja P1
#  Ha ganado el P1
#- Si quieres, puedes controlar errores en la entrada de datos.   
#- Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.   

from enum import Enum

class Player(Enum):
    P1 = 1
    P2 = 2

def tenis_game(points: list):
    game = ["Love", "15", "30", "40"]
    p1_points = 0
    p2_points = 0
    finished = False

    for player in points:

        p1_points += 1 if player == Player.P1 else 0
        p2_points += 1 if player == Player.P2 else 0

        if p1_points >= 3 and p2_points >= 3:
            if not finished and abs(p1_points - p2_points) <= 1:
                print("Deuce" if p1_points == p2_points else "Ventaja P1" if p1_points > p2_points else "Ventaja P2")
            else:
                finished = True
                break
        else:
            if abs(p1_points - p2_points) > 3:
                finished = True
                break
            print(f"{game[p1_points]} - {game[p2_points]}")

    print("Partida incompleta" if not finished else "Ha ganado el P1" if p1_points > p2_points else "Ha ganado el P2")


print("GAME 1")
tenis_game([Player.P1, Player.P1, Player.P2, Player.P2,
            Player.P1, Player.P2, Player.P1, Player.P1])

print("GAME 2")
tenis_game([Player.P1, Player.P1, Player.P2, Player.P2,
           Player.P1, Player.P2, Player.P1, Player.P2, Player.P2, Player.P2])

print("GAME 3")
tenis_game([Player.P1, Player.P1, Player.P1, Player.P1, Player.P1, Player.P1])

print("GAME 4")
tenis_game([Player.P1, Player.P1, Player.P1])