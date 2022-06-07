from django import forms
#Creamos los formularios para cada modelo
class ArtistForm(forms.Form):
    name = forms.CharField()
    nacionality = forms.CharField()

class LabelForm(forms.Form):
    name = forms.CharField()
    country = forms.CharField()

class InstrumentForm(forms.Form):
    name = forms.CharField()
    type = forms.CharField()

class GenreForm(forms.Form):
    name = forms.CharField()
    country_of_origin = forms.CharField()
    
        