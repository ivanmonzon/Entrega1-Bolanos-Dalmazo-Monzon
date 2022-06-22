from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#Creamos los formularios para cada modelo
class ArtistForm(forms.Form):
    name = forms.CharField()
    nacionality = forms.CharField()

class LabelForm(forms.Form): #No se utiliza más, ahora utilizamos LabelCreate en views
    name = forms.CharField()
    country = forms.CharField()

class InstrumentForm(forms.Form):
    name = forms.CharField()
    type = forms.CharField()

class GenreForm(forms.Form):
    name = forms.CharField()
    country_of_origin = forms.CharField()

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repeat Password", widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}

    
        