from django.contrib import admin
from django.urls import path, include
#linkeamos el url admin del proyecto con el url de la app, en este caso App1
urlpatterns = [
    path('admin/', admin.site.urls),
    path('App1/', include('App1.urls')),
]

handler404 = 'App1.views.error_404_view'