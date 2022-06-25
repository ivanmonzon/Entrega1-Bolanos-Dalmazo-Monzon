from django.contrib import admin
from .models import *
# Registramos nuestros modelos
admin.site.register(Artist)
admin.site.register(Label)
admin.site.register(Genre)
admin.site.register(Instrument)