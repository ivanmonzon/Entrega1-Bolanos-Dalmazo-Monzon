from audioop import reverse
from django.shortcuts import render
#Importamos los modelos
from App1.models import Artist, Label, Instrument, Genre
from django.http import HttpResponse
#importamos los formularios
from App1.forms import ArtistForm, LabelForm, InstrumentForm, GenreForm, UserRegisterForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Empezamos a crear las vistas necesarias

def index(request):
    return render(request, "App1/index.html")
#Comenzamos con las vistas relacionados a los artistas, en esta primera view tenemos la opción de buscar al artista

def error_404_view(request, exception):
    return render(request, "App1/404.html")

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
@login_required
def artistForm(request):
    if request.method == 'POST':
        myForm = ArtistForm(request.POST)
        if myForm.is_valid():
            info = myForm.cleaned_data
            artist = Artist (name=info['name'], nacionality=info['nacionality'], biography=info['biography'])
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
@login_required
def labelForm(request): #VIEJO, el nuevo es label_form que utiliza el CreateView
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
@login_required
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
@login_required
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


class LabelList(ListView):
    model = Label
    template_name = "App1/listLabels.html"

class LabelDetail(LoginRequiredMixin, DetailView):
    model = Label
    template_name = "App1/label_detail.html"

class LabelCreate(LoginRequiredMixin,CreateView):
    model = Label
    success_url = reverse_lazy('LabelAdded')
    fields = ['name', 'country']

class LabelUpdate(LoginRequiredMixin,UpdateView):
    model = Label
    success_url = reverse_lazy('listLabels')
    fields = ['name', 'country']

class LabelDelete(LoginRequiredMixin,DeleteView):
    model = Label
    success_url = reverse_lazy('listLabels')

class GenreList(ListView):
    model = Genre
    template_name = "App1/listGenre.html"

class GenreDetail(LoginRequiredMixin, DetailView):
    model = Genre
    template_name = "App1/genre_detail.html"

class GenreCreate(LoginRequiredMixin,CreateView):
    model = Genre
    success_url = reverse_lazy('genreAdded')
    fields = ['name', 'country_of_origin']

class GenreUpdate(LoginRequiredMixin,UpdateView):
    model = Genre
    success_url = reverse_lazy('listGenre')
    fields = ['name', 'country_of_origin']

class GenreDelete(LoginRequiredMixin,DeleteView):
    model = Genre
    success_url = reverse_lazy('listGenre')

class ArtistList(ListView):
    model = Artist
    template_name = "App1/listArtist.html"

class ArtistDetail(LoginRequiredMixin, DetailView):
    model = Artist
    template_name = "App1/artist_detail.html"

class ArtistCreate(LoginRequiredMixin,CreateView):
    model = Artist
    success_url = reverse_lazy('artistAdded')
    fields = ['name', 'nacionality', 'biography']

class ArtistUpdate(LoginRequiredMixin,UpdateView):
    model = Artist
    success_url = reverse_lazy('listArtist')
    fields = ['name', 'nacionality', 'biography']

class ArtistDelete(LoginRequiredMixin,DeleteView):
    model = Artist
    success_url = reverse_lazy('listArtist')

class InstrumentList(ListView):
    model = Instrument
    template_name = "App1/listInstrument.html"

class InstrumentDetail(LoginRequiredMixin, DetailView):
    model = Instrument
    template_name = "App1/instrument_detail.html"

class InstrumentCreate(LoginRequiredMixin,CreateView):
    model = Instrument
    success_url = reverse_lazy('instrumentAdded')
    fields = ['name', 'type']

class InstrumentUpdate(LoginRequiredMixin,UpdateView):
    model = Instrument
    success_url = reverse_lazy('listInstrument')
    fields = ['name', 'type']

class InstrumentDelete(LoginRequiredMixin,DeleteView):
    model = Instrument
    success_url = reverse_lazy('listInstrument')

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            user = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            auth = authenticate(username=user, password=password)

            if auth is not None:
                login(request,auth)
                return render(request,"App1/index.html", {"message":f"Welcome {user}!"})
        else:
            return render(request,"App1/index.html", {"message":"Error, wrong username or password"})                    
    form = AuthenticationForm()
    return render(request,"App1/login.html", {'form':form})

def sign_up(request):
    if request.method == "POST":
        #form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['username']
            form.save()
            return render(request,"App1/index.html", {"message":"User created"})
    else:
        #form = UserCreationForm()
        form = UserRegisterForm()
    return render(request, "App1/sign_up.html", {'form':form})             

