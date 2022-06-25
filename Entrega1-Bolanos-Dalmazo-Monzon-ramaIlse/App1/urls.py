#Acá importamos el path y las vistas
from django.urls import path
from App1 import views
from django.contrib.auth.views import LogoutView

#declaramos los urls para cada vista
urlpatterns = [
    path('', views.index, name="Index"),
    path('artists/', views.artists, name="Artists"),
    path('artistForm/', views.artistForm, name = "ArtistForm"),
    path('artistAdded/', views.artistAdded, name="ArtistAdded"),
    path('artistResult/', views.artistResult),
    path('labels/', views.labels, name="Labels"),
    path('labelForm/', views.labelForm, name = "LabelForm"), #FORM viejo, el nuevo es label_form que utiliza CreateView
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
    path('listLabels/', views.LabelList.as_view(), name='listLabels'),
    path('label_detail/<pk>', views.LabelDetail.as_view(), name='LabelDetail'),
    path('label_form/', views.LabelCreate.as_view(), name='LabelCreate'),
    path('label_update/<pk>', views.LabelUpdate.as_view(), name='LabelUpdate'), 
    path('label_delete/<pk>', views.LabelDelete.as_view(), name='LabelDelete'),
    path('listGenre/', views.GenreList.as_view(), name='listGenre'),
    path('genre_detail/<pk>', views.GenreDetail.as_view(), name='GenreDetail'),
    path('genre_form/', views.GenreCreate.as_view(), name='GenreCreate'),
    path('genre_update/<pk>', views.GenreUpdate.as_view(), name='GenreUpdate'), 
    path('genre_delete/<pk>', views.GenreDelete.as_view(), name='GenreDelete'),
    path('listArtist/', views.ArtistList.as_view(), name='listArtist'),
    path('artist_detail/<pk>', views.ArtistDetail.as_view(), name='ArtistDetail'),
    path('artist_form/', views.ArtistCreate.as_view(), name='ArtistCreate'),
    path('artist_update/<pk>', views.ArtistUpdate.as_view(), name='ArtistUpdate'), 
    path('artist_delete/<pk>', views.ArtistDelete.as_view(), name='ArtistDelete'),
    path('listInstrument/', views.InstrumentList.as_view(), name='listInstrument'),
    path('instrument_detail/<pk>', views.InstrumentDetail.as_view(), name='InstrumentDetail'),
    path('instrument_form/', views.InstrumentCreate.as_view(), name='InstrumentCreate'),
    path('instrument_update/<pk>', views.InstrumentUpdate.as_view(), name='InstrumentUpdate'), 
    path('instrument_delete/<pk>', views.InstrumentDelete.as_view(), name='InstrumentDelete'),
    path('login/', views.login_request, name='Login'),
    path('sign_up/', views.sign_up, name = 'SignUp'),
    path('logout/', LogoutView.as_view(template_name='App1/logout.html'), name = 'Logout'),
]

