# capa de vista/presentación

from django.shortcuts import redirect, render
from .layers.services import services
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate # importamos login y authenticate para poder loguear al usuario luego de autenticar sus datos
from django.core.paginator import Paginator # Importamos paginator para poder desarrollar un paginador
from .forms import CustomUserCreationForm # importamos la funcion que desarrollamos para crear nuevos usuarios
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail


def index_page(request):
    return render(request, 'index.html')

# esta función obtiene 2 listados que corresponden a las imágenes de la API y los favoritos del usuario, y los usa para dibujar el correspondiente template.
# si el opcional de favoritos no está desarrollado, devuelve un listado vacío.
def home(request):

    images = services.getAllImages()
    images_page = Paginator(images, 20) # mostramos 20 cards por pagina
    page = request.GET.get('page') # obtenemos la pagina actual en la que nos encontramos
    images_obj = images_page.get_page(page)
    favourite_list = services.getAllFavourites(request) # Llamamos a la funcion de obtener todos los favoritos


    return render(request, 'home.html', { 'images': images_obj, 'favourite_list': favourite_list })

def search(request):
    search_msg = request.POST.get('query', '')

    # si el texto ingresado no es vacío, trae las imágenes y favoritos desde services.py,
    # y luego renderiza el template (similar a home).
    if (search_msg != ''):
        images = services.getAllImages(search_msg) # llamamos a la funcion de obtener todas las imagenes usando el input del cuadro de busqueda
        images_page = Paginator(images, 20) # mostramos 20 cards por pagina
        page = request.GET.get('page') # obtenemos la pagina actual en la que nos encontramos
        images_obj = images_page.get_page(page)

        # llamamos a la lista de favoritos para que se muestren correctamente cuando utilizamos la barra de busqueda
        favourite_list = services.getAllFavourites(request)
        return render(request, 'home.html', {'images': images_obj, 'favourite_list': favourite_list})
    else:
        return redirect('home')


# Estas funciones se usan cuando el usuario está logueado en la aplicación.
@login_required
def getAllFavouritesByUser(request): # llamamos a la funcion de obtener todos los favoritos de un usuario para mostrarlos en otra plantilla
    favourite_list = services.getAllFavourites(request)
    return render(request, 'favourites.html', { 'favourite_list': favourite_list })

@login_required 
def saveFavourite(request): # llamamos a la funcion agregar favoritos desde servicios
    services.saveFavourite(request)
    return redirect('home') # redireccionamos a la pagina 'home' para seguir viendo las imagenes

@login_required
def deleteFavourite(request): # llamamos a la funcion eliminar favoritos
    services.deleteFavourite(request) 
    return redirect('favoritos') # redireccionamos a la pagina de favoritos para seguir viendo el listado de favs

@login_required
def exit(request): # llamamos a la funcion logout para desloguear
    logout(request)
    return redirect('login') # redireccionamos a la pagina de 'login' una vez deslogueado


# Funcion para la creacion de usuarios
def register(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)

        # En esta seccion desarrollamos todo lo necesario para el registro y el envio de mail
        if user_creation_form.is_valid():
            user_creation_form.save()
            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            # obtenemos los datos que vamos a utilizar para enviar el mail
            user_first_name = user.first_name
            username = user.username
            user_password = user_creation_form.cleaned_data['password1']

            subject = 'TP Rick and Morty'
            message = f"""
            ¡Hola {user_first_name}! Gracias por registrarte.
            Sus datos para iniciar sesion son los siguientes, no los olvides:\n
            USUARIO: {username}
            CONTRASEÑA: {user_password}"""

            recipient = user_creation_form.cleaned_data['email']
            send_mail(subject, message, settings.EMAIL_HOST_USER, [recipient], fail_silently=False)

            login(request, user)
            return redirect('index-page')

    return render(request, 'registration/register.html', data)