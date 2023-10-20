from django.urls import path
from NewApp import views


urlpatterns = [
path("crear padrino/", views.PadrinoCreateView.as_view() ,name = "crear padrino"), 
path("padrino/<int:pk>/", views.PadrinoDetailView.as_view() ,name ="detail padrino"),
path("padrino/", views.PadrinoListView.as_view() ,name ="listar padrino"),
path("padrino/<int:pk>/editar", views.PadrinoUpdateView.as_view() ,name ="update_padrino"),
]