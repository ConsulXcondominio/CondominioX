from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView,ListView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy


from apps.usuario.forms import RegistroForm


#from apps.usuario.forms import RegistroForm
#from apps.usuario.serializers import UserSerializer

#clase para listar todos los registros.
class Registro_list(ListView):
	model = User
	template_name = "usuario/usuario_list.html"




class RegistroUsuario(CreateView):
	model = User
	template_name = "usuario/registrar.html"
	form_class = RegistroForm
	success_url = reverse_lazy('usuario:usuario_listar')



# clase para editar
class Registro_editar(UpdateView):
	model =User
	form_class = RegistroForm
	template_name = 'usuario/usuario_form.html'  #NOTA :: Nombre de la carpeta contenededora y el nombre de el formulario html
	success_url = reverse_lazy('usuario:usuario_listar')




# clase para eliminar
class Registro_eliminar(DeleteView):
	model = User
	template_name = 'usuario/usuario_delete.html'
	success_url = reverse_lazy('usuario:usuario_listar')


