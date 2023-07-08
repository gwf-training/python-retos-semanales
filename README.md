# Retos semanales

### Reto #0: EL FAMOSO "FIZZ BUZZ"
#### Publicación: 26/12/22 | FÁCIL
```
Escribe un programa que muestre por consola los números de 1 a 100 (ambos incluidos y con un salto de línea entre cada impresión), sustituyendo los siguientes:
- Múltiplos de 3 por la palabra "fizz".
- Múltiplos de 5 por la palabra "buzz".
- Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
```

### Reto #1: EL "LENGUAJE HACKER"
#### Publicación: 02/01/23 | FÁCIL
```
Escribe un programa que reciba un texto y transforme lenguaje natural a "lenguaje hacker" (conocido realmente como "leet" o "1337"). 
Este lenguaje se caracteriza por sustituir caracteres alfanuméricos.
- Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) con el alfabeto y los números en "leet".
  (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
```

### Reto #2: EL PARTIDO DE TENIS
#### Publicación: 09/01/23 | MEDIA
```
Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien gane cada punto del juego.
  - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
  - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
      15 - Love
      30 - Love
      30 - 15
      30 - 30
      40 - 30
      Deuce
      Ventaja P1
      Ha ganado el P1
  - Si quieres, puedes controlar errores en la entrada de datos.
  - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.   
```

### Reto #3: EL GENERADOR DE CONTRASEÑAS
#### Publicación: 16/01/23 | MEDIA
```
Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
Podrás configurar generar contraseñas con los siguientes parámetros:
- Longitud: Entre 8 y 16.
- Con o sin letras mayúsculas.
- Con o sin números.
- Con o sin símbolos.
(Pudiendo combinar todos estos parámetros entre ellos)
```

#### Reto #4: PRIMO, FIBONACCI Y PAR
#### Publicación: 23/01/23 | MEDIA

```
Escribe un programa que, dado un número, compruebe y muestre si es primo,
fibonacci y par.
Ejemplos:
- Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
- Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
```

### Reto #6: PIEDRA, PAPEL, TIJERA, LAGARTO, SPOCK
#### Publicación: 06/02/23 | MEDIA
Crea un programa que calcule quien gana más partidas al piedra, papel, tijera, lagarto, spock.
```
- El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
- La función recibe un listado que contiene pares, representando cada jugada.
- El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
  "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
- Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
- Debes buscar información sobre cómo se juega con estas 5 posibilidades.
```

### Reto #7: EL SOMBRERO SELECCIONADOR
#### Publicación: 13/02/23 | MEDIA
```
Crea un programa que simule el comportamiento del sombrero selccionador del universo mágico de Harry Potter.
- De ser posible realizará 5 preguntas (como mínimo) a través de la terminal.
- Cada pregunta tendrá 4 respuestas posibles (también a selecciona una a través de terminal).
- En función de las respuestas a las 5 preguntas deberás diseñar un algoritmo que
  coloque al alumno en una de las 4 casas de Hogwarts:
  (Gryffindor, Slytherin , Hufflepuff y Ravenclaw)
- Ten en cuenta los rasgos de cada casa para hacer las preguntas
  y crear el algoritmo seleccionador:
  Por ejemplo, en Slytherin se premia la ambición y la astucia.
```

### Reto #8: EL GENERADOR PSEUDOALEATORIO
#### Publicación: 20/02/23 | MEDIA
```
Crea un generador de números pseudoaleatorios entre 0 y 100.
- No puedes usar ninguna función "random" (o semejante) del lenguaje de programación seleccionado.
```

### Reto #9: HETEROGRAMA, ISOGRAMA Y PANGRAMA
#### Publicación: 27/02/23 | FACIL
```
Crea 3 funciones, cada una encargada de detectar si una cadena de texto es un heterograma, un isograma o un pangrama.
- Debes buscar la definición de cada uno de estos términos.
```

### Reto #10: LA API
#### Publicación: 06/03/23 | MEDIA
```
Llamar a una API es una de las tareas más comunes en programación.
Implementa una llamada HTTP a una API (la que tú quieras) y muestra su resultado a través de la terminal. 
Por ejemplo: Pokémon, Marvel...
Aquí tienes un listado de posibles APIs: 
- https://github.com/public-apis/public-apis
```

### Reto #11: URL PARAMS
#### Publicación: 13/03/23 | FÁCIL
```
Dada una URL con parámetros, crea una función que obtenga sus valores.
No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.

Ejemplo: En la url https://retosdeprogramacion.com?year=2023&challenge=0
los parámetros serían ["2023", "0"]
```