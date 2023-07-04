#Reto #6: PIEDRA, PAPEL, TIJERA, LAGARTO, SPOCK
#Publicación: 06/02/23 | MEDIA
#Crea un programa que calcule quien gana más partidas al piedra, papel, tijera, lagarto, spock.
#- El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
#- La función recibe un listado que contiene pares, representando cada jugada.
#- El par puede contener combinaciones de "🗿" (piedra), "📄" (papel), "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
#- Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
#- Debes buscar información sobre cómo se juega con estas 5 posibilidades.

from enum import Enum

class Winner(Enum):
    TIE = "Tie"
    PLAYER_1 = "Player 1"
    PLAYER_2 = "Player 2"

class Element(Enum):
    PIEDRA = "🗿"
    PAPEL = "📄"
    TIJERA = "✂️"
    LAGARTO = "🦎"
    SPOCK = "🖖"

RULES = {
    Element.PIEDRA.value: [Element.TIJERA.value, Element.LAGARTO.value],
    Element.PAPEL.value: [Element.PIEDRA.value, Element.SPOCK.value],
    Element.TIJERA.value: [Element.PAPEL.value, Element.LAGARTO.value],
    Element.LAGARTO.value: [Element.SPOCK.value, Element.PAPEL.value],
    Element.SPOCK.value: [Element.PIEDRA.value, Element.TIJERA.value]
}

def analizar_partida(partida: tuple) -> Winner:
    elemento_jugador1, elemento_jugador2 = partida
    if elemento_jugador1 == elemento_jugador2: return Winner.TIE
    return Winner.PLAYER_1 if elemento_jugador2 in RULES.get(elemento_jugador1) else Winner.PLAYER_2

def jugar(partidas: list):
    puntos_jugador1 = 0
    puntos_jugador2 = 0
    for partida in partidas:
        resultado = analizar_partida(partida)
        puntos_jugador1 += 1 if resultado == Winner.PLAYER_1 else 0
        puntos_jugador2 += 1 if resultado == Winner.PLAYER_2 else 0
    return (Winner.PLAYER_1 if puntos_jugador1 > puntos_jugador2 else Winner.PLAYER_2 if puntos_jugador2 > puntos_jugador1 else Winner.TIE).value

print(jugar([("🗿", "🗿")])) #Empate
print(jugar([("🗿", "✂️")])) # gana jugador 1
print(jugar([("✂️", "🗿")])) # gana jugador 2
print(jugar([("🗿", "🗿"), ("🗿", "🗿"), ("🗿", "🗿"), ("🗿", "🗿")])) # empate
print(jugar([("🖖", "🗿"), ("✂️", "📄"), ("🗿", "🗿"), ("🦎", "🖖")])) # gana jugador 1