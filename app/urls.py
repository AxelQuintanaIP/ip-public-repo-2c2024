from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_page, name='index-page'),
    path('login/', views.index_page, name='login'),
    path('home/', views.home, name='home'),
    path('buscar/', views.search, name='buscar'),

    path('favourites/', views.getAllFavouritesByUser, name='favoritos'),
    path('favourites/add/', views.saveFavourite, name='agregar-favorito'),
    path('favourites/delete/', views.deleteFavourite, name='borrar-favorito'),
    
    path('register/', views.register, name="register"), # agregamos un path a la nueva template de registro
    path('subscribe/', views.subscribe, name="subscribe"), # agreagamos un path para la funcion de enviar email

    path('exit/', views.exit, name='exit'),
]