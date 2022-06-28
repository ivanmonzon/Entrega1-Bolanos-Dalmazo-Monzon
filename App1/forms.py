from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#Creamos los formularios para cada modelo
class ArtistForm(forms.Form):
    name = forms.CharField()
    nacionality = forms.CharField()
    biography = forms.TextInput()
class LabelForm(forms.Form): #No se utiliza más, ahora utilizamos LabelCreate en views
    name = forms.CharField()
    country = forms.CharField()
    description = forms.TextInput()
class InstrumentForm(forms.Form):
    name = forms.CharField()
    type = forms.CharField()
    description = forms.TextInput()
class GenreForm(forms.Form):
    name = forms.CharField()
    country_of_origin = forms.CharField()
    description = forms.TextInput()
class UserRegisterForm(UserCreationForm):
    name = forms.CharField()
    lastname = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repeat Password", widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['name','lastname','username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}

class UserEditForm(UserCreationForm):
    first_name = forms.CharField(label="Name")
    last_name = forms.CharField(label="Last Name")
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Change Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repeat Password", widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['first_name','last_name','username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}    
        