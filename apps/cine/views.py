from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
from django.urls import reverse_lazy
from .models import Local
from .forms import LocalForm
from .models import Funcion
from .forms import FuncionForm


# Create your views here.
class Home(TemplateView):
    template_name = 'cine/index.html'

    def get_context_data(self, *args, **kwargs):
        locales = Local.objects.all()
        context = super(Home,self).get_context_data(*args, **kwargs)
        context['locales'] = locales
        return context

class ListarLocales(ListView):
    model = Local
    template_name = 'cine/local/listar_local.html'
    queryset = Local.objects.all()
    context_object_name = 'locales'

class CrearLocal(CreateView):
    model = Local
    form_class = LocalForm
    template_name = 'cine/local/crear_local.html'
    success_url = reverse_lazy('cine:listar_locales')

class CrearFuncion(CreateView):
    model = Funcion
    form_class= FuncionForm
    template_name = 'cine/local/crear_funcion.html'
    success_url = reverse_lazy('cine:listar_funcion')
