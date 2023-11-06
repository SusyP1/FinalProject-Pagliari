from django.urls import path, include
# from DogsApp.views import pruebaview2
from DogsApp.views import inicioview
from DogsApp.views import aboutmeview
from DogsApp.views import adoptado_view
from DogsApp.views import adoptante_view
from DogsApp.views import refugio_view
from DogsApp.views import busquedaview
from DogsApp.views import leerview
from DogsApp.views import loginview
from DogsApp.views import registroview
from django.contrib.auth.views import LogoutView
from DogsApp.views import editarview
from DogsApp.views import cambiarpassview
from DogsApp.views import editaradoptadoview
from DogsApp.views import mascotasview
from DogsApp.views import usuarioview
from DogsApp.views import eliminaradoptadoview
from DogsApp.views import detalledoptadoview
from DogsApp.views import detalleusuarioview
from DogsApp.views import detalleusuarioview
from DogsApp.views import SendMessageView
from DogsApp.views import MessageListView
from DogsApp.views import create_blog_post




# from django.conf import settings
# from django.conf.urls.static import static



urlpatterns = [
    path("", inicioview, name="inicio"),
    path("mascotas/", mascotasview, name="mascotas"),
    path("usuario/", usuarioview, name="usuario"),   
    path('about_me/', aboutmeview, name="about me"),
    # path("prueba2/", pruebaview2, name="prueba2"),
    path('mascotas/adoptado/', adoptado_view,name="crear adoptado"),
    path('adoptante/', adoptante_view,name="adoptante"),
    path('refugio/', refugio_view,name="refugio"),
    path("listado_animales/",leerview,name="listado animales"),
    path("busqueda/",busquedaview,name="busqueda adoptado"),
    path("login/",loginview,name="login"),
    path("registro/",registroview,name="registro"),
    path("logout/",LogoutView.as_view(template_name="temp_app/logout.html")),
    path("editar_perfil/",editarview,name="editar perfil"),
    path("cambiar_password/",cambiarpassview.as_view(),name="cambiar password"),
    path("mascotas/editar_adoptado/<int:adoptado_id>",editaradoptadoview,name="editar adoptado"),
    path("eliminar_adoptado/<int:adoptado_nombre>",eliminaradoptadoview,name="eliminar adoptado"),
    path("detalle_adoptado/<int:adoptado_id>",detalledoptadoview,name="detalle adoptado"),
    path("detalle_usuario/",detalleusuarioview,name="detalle usuario"),
    path("mensajes/", SendMessageView.as_view(), name='send_message'),
    path("listado/", MessageListView.as_view() , name = "listado"),
    path('blogspot/', create_blog_post, name="create_blog_post"),
    

    
           
]
   
# urlpatterns= static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)