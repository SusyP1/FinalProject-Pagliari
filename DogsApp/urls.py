from django.urls import path, include
from DogsApp.views import pruebaview2
from DogsApp.views import inicioview
from DogsApp.views import pruebaview
from DogsApp.views import adoptado_view
from DogsApp.views import adoptante_view
from DogsApp.views import refugio_view
from DogsApp.views import busquedaview



urlpatterns = [
    path("", inicioview, name="inicio"),
    path('prueba/', pruebaview, name="prueba"),
    path("prueba2/", pruebaview2, name="prueba2"),
    path('adoptado/', adoptado_view,name="adoptado"),
    path('adoptante/', adoptante_view,name="adoptante"),
    path('refugio/', refugio_view,name="refugio"),
    path("busqueda_adoptado/",busquedaview,name="busqueda adoptado")
]
   