# capa de transporte/comunicación con otras interfaces o sistemas externos.

import requests
from ...config import config

# comunicación con la REST API.
# este método se encarga de "pegarle" a la API y traer una lista de objetos JSON crudos (raw).
def getAllImages(input=None):

    json_collection = []
    json_response = []
    total_pages = 42
    default_url = "https://rickandmortyapi.com/api/character?page="
    search_url = config.DEFAULT_REST_API_SEARCH
    
    for page in range(1, total_pages + 1):
        if input is None:
            url = f'{default_url} + {page}'
        else:
            url = f'{search_url} + {input}'
        response = requests.get(url)
        json_response = response.json()

        # si la búsqueda no arroja resultados, entonces retornamos una lista vacía de elementos.
        if 'error' in json_response:
            print("[transport.py]: la búsqueda no arrojó resultados.")
            return json_collection

        for object in json_response['results']:
            try:
                if 'image' in object and object not in json_collection:  # verificar si la clave 'image' está presente en el objeto (sin 'image' NO nos sirve, ya que no mostrará las imágenes).
                    json_collection.append(object)
                else:
                    print("[transport.py]: se encontró un objeto sin clave 'image', omitiendo...")

            except KeyError: 
                # puede ocurrir que no todos los objetos tenga la info. completa, en ese caso descartamos dicho objeto y seguimos con el siguiente en la próxima iteración.
                pass

    return json_collection