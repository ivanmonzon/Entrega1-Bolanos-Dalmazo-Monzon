#Acá importamos el path y las vistas
from django.urls import path
from App1 import views
#declaramos los urls para cada vista
urlpatterns = [
    path('', views.index, name="Index"),
    path('artists/', views.artists, name="Artists"),
    path('artistForm/', views.artistForm, name = "ArtistForm"),
    path('artistAdded/', views.artistAdded, name="ArtistAdded"),
    path('artistResult/', views.artistResult),
    path('labels/', views.labels, name="Labels"),
    path('labelForm/', views.labelForm, name = "LabelForm"),
    path('labelAdded/', views.labelAdded, name="LabelAdded"),
    path('labelResult/', views.labelResult),       
    path('genres/', views.genres, name="Genres"),
    path('genreForm/', views.genreForm, name = "GenreForm"),
    path('genreAdded/', views.genreAdded, name="GenreAdded"),
    path('genreResult/', views.genreResult),
    path('instruments/', views.instruments, name="Instruments"),
    path('instrumentForm/', views.instrumentForm, name = "InstrumentForm"),
    path('instrumentAdded/', views.instrumentAdded, name="InstrumentAdded"),
    path('instrumentResult/', views.instrumentResult),
    
]
