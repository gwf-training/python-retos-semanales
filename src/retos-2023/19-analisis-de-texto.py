
### Reto #19: ANÁLISIS DE TEXTO
#### Publicación: 11/05/23 | MEDIA
#
#Crea un programa que analice texto y obtenga:
#- Número total de palabras.
#- Longitud media de las palabras.
#- Número de oraciones del texto (cada vez que aparecen un punto).
#- Encuentre la palabra más larga.
#
#Todo esto utilizando un único bucle.

def analizar_texto(texto: str):
    palabras = list()
    palabra_list = list()
    count_puntos = 0
    palabra_mas_larga = ""
    sum_logitud_palabras = 0
    for caracter in texto:
        # contar cada vez que aparece un punto saber la cantidad de oraciones
        if caracter == '.':
            count_puntos += 1

        # encontrar todas la palabras
        if caracter not in [' ', '\t', '\n']:
            if caracter not in ('.', ',', ';','(', ')'):
                palabra_list.append(caracter)
        else:
            if len(palabra_list) > 0:
                palabra = "".join(palabra_list)
                longitud_palabra = len(palabra)
                sum_logitud_palabras += longitud_palabra
                #encontrar la palabra más larga.
                if (longitud_palabra > len(palabra_mas_larga)):
                    palabra_mas_larga = str(palabra)

                palabras.append(palabra)
                palabra_list = list()


    # analisis ultima palabra
    if len(palabra_list) > 0:
        palabra = "".join(palabra_list)
        longitud_palabra = len(palabra)
        sum_logitud_palabras  += longitud_palabra
        if (longitud_palabra > len(palabra_mas_larga)):
            palabra_mas_larga = str(palabra)
        palabras.append(palabra)
        count_puntos += 1

    cantidad_palabras = len(palabras)

    print('Cantidad de palabras: ', cantidad_palabras)
    print('Longitud media de las palabras:', sum_logitud_palabras // cantidad_palabras)
    print('Número de oraciones: ', count_puntos)
    print('Palabra más larga: ', palabra_mas_larga)



if __name__ == '__main__':
    print('Reto #19: ANÁLISIS DE TEXTO')
    print('Publicación: 11/05/23 | MEDIA')
    texto = """
AC/DC es una banda de hard rock británica-australiana, formada en 1973 en Australia por los hermanos escoceses Malcolm Young y Angus Young. Sus álbumes se han vendido en un total estimado de 200 millones de copias, embarcándose en giras multitudinarias por todo el mundo y sus éxitos han musicalizado varias producciones cinematográficas sobresalientes. Son famosas sus actuaciones en vivo, resultando vibrantes y exultantes espectáculos de primer orden. Mucho de ello se debe al extravagante estilo de su guitarrista principal y símbolo visual, Angus Young, quien asume el rol de guitarrista principal durante los conciertos, gracias a sus dinámicos y adrenalínicos despliegues escénicos uniformado de colegial callejero.Al comienzo, los conciertos y tiempos por los cuales sufrieron diversos cambios en su alineación. En 1974, la llegada del cantante Bon Scott se convertiría en una pieza clave del éxito del grupo. Su presencia en escena, lo convirtió en uno de los personajes más carismáticos de la historia del hard rock. La formación se estabilizaría con Cliff Williams (bajo) y Phil Rudd (baterista).
En 1974 incursionaron por primera vez fuera de los conciertos en bandas de punk rock locales, que ofrecían un contrapunto sonoro a las ampulosidades y la fastuosidad de las bandas que triunfaron en el mercado de la época. Ese mismo año se trasladaron a Glasgow, de donde procedían Desembarcaron en pleno auge del punk rock, lo que contribuyó a que, en poco tiempo, obtuvieran una enorme aceptación del público, ocupando inmediatamente los primeros puestos en ventas.
    """    
    texto = 'AC/DC es una banda de hard rock británica-australiana'
    analizar_texto(texto)