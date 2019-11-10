from django import forms
from .models import Local

from .models import Sala
from .models import Funcion
from .models import Actor
from .models import Pelicula

from .models import Venta



class LocalForm(forms.ModelForm):
    class Meta:
        model = Local
        fields = ['nombre', 'direccion', 'tiposervicio', 'precio','distrito']


class SalaForm(forms.ModelForm):
    class Meta:
        model = Sala
        fields = ['nombre']


class FuncionForm(forms.ModelForm):
    class Meta:
        model = Funcion
        fields = ['id_local', 'id_sala', 'hora_funcion','id_pelicula' ]


class ActorForm(forms.ModelForm):
    class Meta:
        model = Actor
        fields = ['nombre', 'imagen']

class PeliculaForm(forms.ModelForm):
    class Meta:
        model = Pelicula
        fields = ['id_local','trailer', 'titulo','genero','duracion','categoria','imagen','psinosis','idioma']

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['id_usuario','fecha_venta','id_funcion','cantidad'] 
