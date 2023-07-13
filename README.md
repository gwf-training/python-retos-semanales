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

Ejemplo: En la url https://retosdeprogramacion.com?year=2023&challenge=0 los parámetros serían ["2023", "0"]
```

### Reto #12: VIERNES 13
####FÁCIL | Publicación: 20/03/23 | Resolución: 27/03/23
```
Crea una función que sea capaz de detectar si existe un viernes 13 en el mes y el año indicados.
- La función recibirá el mes y el año y retornará verdadero o falso.
```

### Reto #13: ADIVINA LA PALABRA
#### Publicación: 27/03/23 | FÁCIL
```
Crea un pequeño juego que consista en adivinar palabras en un número máximo de intentos:
- El juego comienza proponiendo una palabra aleatoria incompleta
  - Por ejemplo "m_ur_d_v", y el número de intentos que le quedan
- El usuario puede introducir únicamente una letra o una palabra (de la misma longitud que la palabra a adivinar)
  - Si escribe una letra y acierta, se muestra esa letra en la palabra. Si falla, se resta uno al número de intentos
  - Si escribe una resolución y acierta, finaliza el juego, en caso contrario, se resta uno al número de intentos
  - Si el contador de intentos llega a 0, el jugador pierde
- La palabra debe ocultar de forma aleatoria letras, y nunca puede comenzar ocultando más del 60%
- Puedes utilizar las palabras que quieras y el número de intentos que consideres
```

### Reto #14: OCTAL Y HEXADECIMAL
#### Publicación: 03/04/23 | FÁCIL
```
Crea una función que reciba un número decimal y lo trasforme a Octal y Hexadecimal.
- No está permitido usar funciones propias del lenguaje de programación que realicen esas operaciones directamente.
```
### Reto #15: AUREBESH
#### Publicación: 10/04/23 | FÁCIL
```
Crea una función que sea capaz de transformar Español al lenguaje básico del universo Star Wars: el "Aurebesh".
- Puedes dejar sin transformar los caracteres que no existan en "Aurebesh".
- También tiene que ser capaz de traducir en sentido contrario.
 
¡Que la fuerza os acompañe!
 ```

### Reto #16: LA ESCALERA
#### Publicación: 17/04/23 | MEDIA
```
Crea una función que dibuje una escalera según su número de escalones.
- Si el número es positivo, será ascendente de izquiera a derecha.
- Si el número es negativo, será descendente de izquiera a derecha.
- Si el número es cero, se dibujarán dos guiones bajos(__).

Ejemplo: 4
        _
      _|
    _|
  _|
_|
```

### Reto #17: GIT Y GITHUB
#### Publicación: 24/04/23 | DIFÍCIL
```
¿Sabías que puedes leer información de Git y GitHub desde la gran mayoría de lenguajes de programación?
Crea un programa que lea los últimos 10 commits de este repositorio y muestre:
- Hash
- Autor
- Mensaje
- Fecha y hora

Ejemplo de salida:
Commit 1 (el más reciente) | 12345A | MoureDev | Este es un commit | 24/04/2023 21:00
 
Se permite utilizar librerías que nos faciliten esta tarea.
```

### Reto #18: WEB SCRAPING
#### Publicación: 01/05/23 | DIFÍCIL
```
El día 128 del año celebramos en la comunidad el "Hola Mundo day"
Vamos a hacer "web scraping" sobre su sitio web: https://holamundo.day
 
Crea un programa que se conecte a la web del evento e imprima únicamente la agenda de eventos
del día 8. Mostrando hora e información de cada uno.
Ejemplo: "16:00 | Bienvenida"

Se permite utilizar librerías que nos faciliten esta tarea.
```

### Reto #19: ANÁLISIS DE TEXTO
#### Publicación: 11/05/23 | MEDIA
```
Crea un programa que analice texto y obtenga:
- Número total de palabras.
- Longitud media de las palabras.
- Número de oraciones del texto (cada vez que aparecen un punto).
- Encuentre la palabra más larga.

Todo esto utilizando un único bucle.
```

### Reto #20: LA TRIFUERZA
#### Publicación: 15/05/23 | MEDIA
```
¡El nuevo "The Legend of Zelda: Tears of the Kingdom" ya está disponible! 
Crea un programa que dibuje una Trifuerza de "Zelda"
formada por asteriscos.
- Debes indicarle el número de filas de los triángulos con un entero positivo (n).
- Cada triángulo calculará su fila mayor utilizando la fórmula 2n-1.
Ejemplo: Trifuerza 2

    *
   ***
   *
 *** ***

```

### Reto #21: NÚMEROS PRIMOS GEMELOS
#### Publicación: 22/05/23 | MEDIA
```
Crea un programa que encuentre y muestre todos los pares de números primos gemelos en un rango concreto.
El programa recibirá el rango máximo como número entero positivo.

- Un par de números primos se considera gemelo si la diferencia entre ellos es exactamente 2. 
  Por ejemplo (3, 5), (11, 13)
- Ejemplo: Rango 14
  (3, 5), (5, 7), (11, 13)
```
