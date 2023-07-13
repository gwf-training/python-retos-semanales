### Reto #18: WEB SCRAPING
#### Publicación: 01/05/23 | DIFÍCIL

#El día 128 del año celebramos en la comunidad el "Hola Mundo day"
#Vamos a hacer "web scraping" sobre su sitio web: https://holamundo.day
# 
#Crea un programa que se conecte a la web del evento e imprima únicamente la agenda de eventos
#del día 8. Mostrando hora e información de cada uno.
#Ejemplo: "16:00 | Bienvenida"

#Se permite utilizar librerías que nos faciliten esta tarea.

#pip install requests
#pip install beautifulsoup4

import requests
from bs4 import BeautifulSoup

def mostrar_agenda():
    url = 'https://holamundo.day'
    response = requests.get(url)
    print("status code:",response.status_code)

    content = response.content # we get all the content from the website
    soup = BeautifulSoup(content, 'html.parser') # beautiful soup will give a chance to parse
    print("title:", soup.title) # <title>"Hola Mundo" day | 8 de mayo | La conferencia de programación de la comunidad para la comunidad</title>
    print("text:", soup.title.get_text()) # "Hola Mundo" day | 8 de mayo | La conferencia de programación de la comunidad para la comunidad
    #print(soup.body) # gives the whole page on the website

    print('\n4 de Mayo')
    #blockquotes = soup.find_all("blockquote")
    blockquotes = soup.find_all("blockquote", class_="BlockquoteElement___StyledBlockquote-sc-1dtx4ci-0 slate-BlockquoteElement notion-quote unset-width")
    #blockquotes = soup.find_all(["h1", "blockquote"], {"data-slate-node" : "element"})
    for blockquote in blockquotes[14:21]:
        print(blockquote.text.replace('\n',' | '))

    print('\n8 de Mayo')
    for blockquote in blockquotes[21:]:
        print(blockquote.text)

if __name__ == '__main__':
    print('Reto #18: WEB SCRAPING')
    print('Publicación: 01/05/23 | DIFÍCIL')
    mostrar_agenda()