# translator: se refiere a un componente o conjunto de funciones que se utiliza para convertir o "mapear" datos de un formato o estructura a otro. Esta conversión se realiza típicamente cuando se trabaja con diferentes capas de una aplicación, como por ejemplo, entre la capa de datos y la capa de presentación, o entre dos modelos de datos diferentes.

from app.layers.utilities.card import Card

# usado cuando la info. viene de la API, para transformarla en una Card.
def fromRequestIntoCard(object):
    card = Card(
            url=object['image'],
            name=object['name'],
            status=object['status'], 
            last_location = object['location']['name'],
            first_seen = object['origin']['name']
    )
    return card

# usado cuando la info. viene del template, para transformarlo en una Card antes de guardarlo en la base de datos.
def fromTemplateIntoCard(home): # emprolijamos y cambiamos por la template 'home'
    card = Card(
        url=home.POST.get("url"),
        name=home.POST.get("name"),
        status=home.POST.get("status"),
        last_location=home.POST.get("last_location"),
        first_seen=home.POST.get("first_seen")
    )
    return card

# cuando la info. viene de la base de datos, para transformarlo en una Card antes de mostrarlo.
def fromRepositoryIntoCard(favourite): # emprolijamos y llamamos al modelo Favourite de la base de datos
    card = Card(
            id=favourite['id'],
            url=favourite['url'],
            name=favourite['name'],
            status=favourite['status'],
            last_location=favourite['last_location'],
            first_seen=favourite['first_seen'],
    )
    return card