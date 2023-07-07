#Reto #10: LA API
#MPublicación: 06/03/23 | MEDIA

#Llamar a una API es una de las tareas más comunes en programación. 
#Implementa una llamada HTTP a una API (la que tú quieras) y muestra su resultado a través de la terminal. 
# Por ejemplo: Pokémon, Marvel...

#Aquí tienes un listado de posibles APIs: 
#https://github.com/public-apis/public-apis
 

#python -m pip install --upgrade pip    
#pip install requests     

import requests

def get_pokemons():
    url = "https://pokeapi.co/api/v2/pokemon?limit=20"
    response = requests.get(url)
    for index, pokemon in enumerate(response.json()["results"]):
        pokemon_name = pokemon["name"]
        print(f"{index + 1}) {pokemon_name}")

def get_starwars_characters():
    url = "https://swapi.dev/api/people/?limit=10&page=2"
    response = requests.get(url)
    for index, character in enumerate(response.json()["results"]):
        character_name = character["name"]
        print(f"{index + 1}) {character_name}")

if __name__ == '__main__':
    get_pokemons()
    get_starwars_characters()