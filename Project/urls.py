from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from App1 import views
#linkeamos el url admin del proyecto con el url de la app, en este caso App1
urlpatterns = [
    path('admin/', admin.site.urls),
    path('App1/', include('App1.urls')),
    path('', views.index, name="Index"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)#agregamos esto para que nos permita traer las imagenes
handler404 = 'App1.views.error_404_view'