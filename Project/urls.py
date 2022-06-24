from django.contrib import admin
from django.contrib.admin import helpers
from django.urls import path, include
from App1 import views
#linkeamos el url admin del proyecto con el url de la app, en este caso App1
urlpatterns = [
    path('admin/', admin.site.urls),
    path('App1/', include('App1.urls')),
    path('', views.index, name="Index"),
]

handler404 = 'App1.views.error_404_view'