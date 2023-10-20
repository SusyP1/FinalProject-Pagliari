from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.views.generic.list import ListView
from NewApp.models import Padrino
from django.urls import reverse_lazy 


# Create your views here.
class PadrinoCreateView(CreateView):
    model = Padrino
    template_nPadrinome = "temp_NApp/crear_padrino.html"
    fields =["apodo","ahijado","descripcion","fecha_inicio"]
    success_url = reverse_lazy("padrino")

class PadrinoDetailView(DetailView):
    model = Padrino
    template_name = "temp_NApp/detail_padrino.html"
    success_url = reverse_lazy("padrino")
    
class PadrinoUpdateView(UpdateView):
    model = Padrino
    template_name = "temp_NApp/update_padrino.html"
    fields =["apodo","ahijado","descripcion","fecha_inicio"]
    success_url = reverse_lazy("padrino")
    
class PadrinoListView(ListView):
    model = Padrino
    template_name = "temp_NApp/listar_padrino.html"
    context_object_name = "listado padrinos"
  

