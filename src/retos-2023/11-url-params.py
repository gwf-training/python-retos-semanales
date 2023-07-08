#Reto #11: URL PARAMS
#Publicación: 13/03/23 | FÁCIL

#Dada una URL con parámetros, crea una función que obtenga sus valores.
#No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.

#Ejemplo: En la url https://retosdeprogramacion.com?year=2023&challenge=0
#los parámetros serían ["2023", "0"]

def get_url_params (url: str) -> list[str]:
    url_split = url.split('?')
    if url_split is not None and len(url_split) <= 1: return []
    params = url_split[1].split('&')
    params_value = list()
    for param in params:
        value_split = param.split('=')
        if value_split is not None and len(value_split) >= 1:
            params_value.append(value_split[1])
    return params_value

if __name__ == "__main__":
    params = get_url_params("https://retosdeprogramacion.com?year=2023&challenge=0")
    print("params:", params)