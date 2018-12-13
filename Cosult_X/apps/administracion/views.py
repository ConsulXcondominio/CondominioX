from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView,CreateView,UpdateView,DeleteView

from apps.administracion.models import Empleado
from  apps.administracion.forms import EmpleadoForm

from apps.administracion.models import Area
from apps.administracion.forms import AreaForm1


from apps.administracion.models import Propietario
from apps.administracion.forms import PropietarioForm
# Create your views here.


from apps.administracion.models import Reserva
from apps.administracion.forms import ReservaForm




from apps.administracion.models import Visita
from apps.administracion.forms import VisitaForm


#clase para listar todos los registros.
class Empleado_list(ListView):
	model = Empleado
	template_name = "administracion/empleado_list.html"



#clase para crear registros.
class Empleado_crear(CreateView):
	model = Empleado
	form_class = EmpleadoForm
	template_name = 'administracion/empleado_form.html'
	success_url = reverse_lazy('empleado:empleado_listar')  # NOTA :: se de ve de colocar el nombre de la url que esta registrado como "namesapace en la urls de Consult_X"





# clase para editar
class Empleado_editar(UpdateView):
	model = Empleado
	form_class = EmpleadoForm
	template_name = 'Administracion/empleado_form.html'  #NOTA :: Nombre de la carpeta contenededora y el nombre de el formulario html
	success_url = reverse_lazy('empleado:empleado_listar')




# clase para eliminar
class Emplado_eliminar(DeleteView):
	model = Empleado
	template_name = 'Administracion/empleado_delete.html'
	success_url = reverse_lazy('empleado:empleado_listar')





##########################################################################
###############################   AREA   #################################


#clase para listar todos los registros.
class Area_list(ListView):
	model = Area
	template_name = "area/area_list.html"



#clase para crear registros.
class Area_crear(CreateView):
	model = Area
	form_class = AreaForm1
	template_name = 'area/area_form.html'
	success_url = reverse_lazy('area:area_listar')  # NOTA :: se de ve de colocar el nombre de la url que esta registrado como "namesapace en la urls de Consult_X"





# clase para editar
class Area_editar(UpdateView):
	model = Area
	form_class = AreaForm1
	template_name = 'area/area_form.html'  #NOTA :: Nombre de la carpeta contenededora y el nombre de el formulario html
	success_url = reverse_lazy('area:area_listar')




# clase para eliminar
class Area_eliminar(DeleteView):
	model =Area
	template_name = 'area/area_delete.html'
	success_url = reverse_lazy('area:area_listar')








##########################################################################
########################   PROPIETARIO   #################################


#clase para listar todos los registros.
class Propietario_list(ListView):
	model = Propietario
	template_name = "propietario/propietario_list.html"



#clase para crear registros.
class Propietario_crear(CreateView):
	model = Propietario
	form_class = PropietarioForm
	template_name = 'propietario/propietario_form.html'
	success_url = reverse_lazy('propietario:propietario_listar')  # NOTA :: se de ve de colocar el nombre de la url que esta registrado como "namesapace en la urls de Consult_X"



# clase para editar
class Propietario_editar(UpdateView):
	model = Propietario
	form_class =PropietarioForm
	template_name = 'propietario/propietario_form.html'  #NOTA :: Nombre de la carpeta contenededora y el nombre de el formulario html
	success_url = reverse_lazy('propietario:propietario_listar')




# clase para eliminar
class Propietario_eliminar(DeleteView):
	model =Propietario
	template_name = 'propietario/propietario_delete.html'
	success_url = reverse_lazy('propietario:propietario_listar')




#########################################################
################ RESERVA  ##############################
#clase para listar todos los registros.
class Reserva_list(ListView):
	model = Reserva
	template_name = "reserva/reserva_list.html"




	# clase para crear registros.
class Reserva_crear(CreateView):
		model = Reserva
		form_class = ReservaForm
		template_name = 'reserva/reserva_form.html'
		success_url = reverse_lazy('reserva:reserva_listar')  # NOTA :: se de ve de colocar el nombre de la url que esta registrado como "namesapace en la urls de Consult_X"





# clase para editar
class Reserva_editar(UpdateView):
	model = Reserva
	form_class =ReservaForm
	template_name = 'reserva/reserva_form.html'  #NOTA :: Nombre de la carpeta contenededora y el nombre de el formulario html
	success_url = reverse_lazy('reserva:reserva_listar')




# clase para eliminar
class Reserva_eliminar(DeleteView):
	model =Reserva
	template_name = 'reserva/reserva_delete.html'
	success_url = reverse_lazy('reserva:reserva_listar')












#clase para listar todos los registros.
class visita_list(ListView):
	model = Visita
	template_name = "visitas/visita_list.html"



#clase para crear registros.
class visita_crear(CreateView):
	model = Visita
	form_class = VisitaForm
	template_name = 'visitas/visita_form.html'
	success_url = reverse_lazy('visita:visita_listar')  # NOTA :: se de ve de colocar el nombre de la url que esta registrado como "namesapace en la urls de Consult_X"





# clase para editar
class visita_editar(UpdateView):
	model = Visita
	form_class = VisitaForm
	template_name = 'visitas/visita_form.html'  #NOTA :: Nombre de la carpeta contenededora y el nombre de el formulario html
	success_url = reverse_lazy('visita:visita_listar')




# clase para eliminar
class visita_eliminar(DeleteView):
	model = Visita
	template_name = 'visitas/visita_delete.html'
	success_url = reverse_lazy('visita:visita_listar')












##########################################################
##################### PAGINA PRINCIPAL####################
def index(request):
    return render(request, 'pagina_principal/index.html')