from django.shortcuts import render
#Importamos los modelos
from App1.models import Artist, Label, Instrument, Genre
from django.http import HttpResponse
#importamos los formularios
from App1.forms import ArtistForm, LabelForm, InstrumentForm, GenreForm
# Empezamos a crear las vistas necesarias
def index(request):
    return render(request, "App1/index.html")
#Comenzamos con las vistas relacionados a los artistas, en esta primera view tenemos la opción de buscar al artista
def artists(request):
    return render(request, "App1/artists.html")
#En esta vista nos arroja el resultado de la busqueda de la vista de arriba
def artistResult(request):
    if request.GET["name"]:
        name = request.GET['name']
        artists =Artist.objects.filter(name__icontains=name)
        return render(request, "App1/artistResult.html", {"artists":artists, "name":name})
    else:
        answer = "You didn't sent any data"
    return HttpResponse(answer)
#Vista para crear el formulario de carga de artistas
def artistForm(request):
    if request.method == 'POST':
        myForm = ArtistForm(request.POST)
        if myForm.is_valid():
            info = myForm.cleaned_data
            artist = Artist (name=info['name'], nacionality=info['nacionality'])
            artist.save()
            return render(request, "App1/artistAdded.html")
    else:
        myForm = ArtistForm()
    return render(request, "App1/artistForm.html", {"myForm":myForm})
#Vista para notificarnos que el artista fue agregado correctamente
def artistAdded(request):
    return render(request, "App1/artistAdded.html")
#En esta view tenemos la opción de buscar al label o sello discográfico
def labels(request):
    return render(request,"App1/labels.html")
#Vista para crear el formulario de carga de labels
def labelForm(request):
    if request.method == 'POST':
        myForm = LabelForm(request.POST)
        if myForm.is_valid():
            info = myForm.cleaned_data
            label = Label(name=info['name'], country=info['country'])
            label.save()
            return render(request, "App1/labelAdded.html")
    else:
        myForm = LabelForm()
    return render(request, "App1/labelForm.html", {"myForm":myForm})
#Vista para notificarnos que el label fue agregado correctamente
def labelAdded(request):
    return render(request, "App1/labelAdded.html")
#En esta vista nos arroja el resultado de la busqueda de labels
def labelResult(request):
    if request.GET["name"]:
        name = request.GET['name']
        labels =Label.objects.filter(name__icontains=name)
        return render(request, "App1/labelResult.html", {"labels":labels, "name":name})
    else:
        answer = "You didn't sent any data"
    return HttpResponse(answer)
#En esta view tenemos la opción de buscar el instrumento musical
def instruments(request):
    return render(request,"App1/instruments.html")
#Vista para crear el formulario de carga de instrumentos
def instrumentForm(request):
    if request.method == 'POST':
        myForm = InstrumentForm(request.POST)
        if myForm.is_valid():
            info = myForm.cleaned_data
            instrument = Instrument(name=info['name'], type=info['type'])
            instrument.save()
            return render(request, "App1/instrumentAdded.html")
    else:
        myForm = InstrumentForm()
    return render(request, "App1/instrumentForm.html", {"myForm":myForm})
#Vista para notificarnos que el instrumento fue agregado correctamente
def instrumentAdded(request):
    return render(request, "App1/instrumentAdded.html")
#En esta vista nos arroja el resultado de la busqueda de instrumentos
def instrumentResult(request):
    if request.GET["name"]:
        name = request.GET['name']
        instruments =Instrument.objects.filter(name__icontains=name)
        return render(request, "App1/instrumentResult.html", {"instruments":instruments, "name":name})
    else:
        answer = "You didn't sent any data"
    return HttpResponse(answer)
#En esta view tenemos la opción de buscar el género musical
def genres(request):
    return render(request,"App1/genres.html")
#Vista para crear el formulario de carga de géneros musicales
def genreForm(request):
    if request.method == 'POST':
        myForm = GenreForm(request.POST)
        if myForm.is_valid():
            info = myForm.cleaned_data
            genre = Genre(name=info['name'], country_of_origin=info['country_of_origin'])
            genre.save()
            return render(request, "App1/genreAdded.html")
    else:
        myForm = GenreForm()
    return render(request, "App1/genreForm.html", {"myForm":myForm}) 
#Vista para notificarnos que el género fue agregado correctamente
def genreAdded(request):
    return render(request, "App1/genreAdded.html")
#En esta vista nos arroja el resultado de la busqueda de géneros musicales
def genreResult(request):
    if request.GET["name"]:
        name = request.GET['name']
        genres =Genre.objects.filter(name__icontains=name)
        return render(request, "App1/genreResult.html", {"genres":genres, "name":name})
    else:
        answer = "You didn't sent any data"
    return HttpResponse(answer)


