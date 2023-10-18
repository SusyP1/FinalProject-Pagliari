from django.urls import path, include
# from DogsApp.views import pruebaview2
from DogsApp.views import inicioview
# from DogsApp.views import pruebaview
from DogsApp.views import adoptado_view
from DogsApp.views import adoptante_view
from DogsApp.views import refugio_view
from DogsApp.views import busquedaview
from DogsApp.views import leerview
from DogsApp.views import loginview
from DogsApp.views import registroview
from django.contrib.auth.views import LogoutView




urlpatterns = [
    path("", inicioview, name="inicio"),
    # path('prueba/', pruebaview, name="prueba"),
    # path("prueba2/", pruebaview2, name="prueba2"),
    path('adoptado/', adoptado_view,name="adoptado"),
    path('adoptante/', adoptante_view,name="adoptante"),
    path('refugio/', refugio_view,name="refugio"),
    path("leer/",leerview,name="leer"),
    path("busqueda/",busquedaview,name="busqueda adoptado"),
    path("login/",loginview,name="login"),
    path("registro/",registroview,name="registro"),
    path("logout/",LogoutView.as_view(template_name="temp_app/logout.html")),
    
]
   