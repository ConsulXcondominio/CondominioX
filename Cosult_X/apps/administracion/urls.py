from django.conf.urls import url



#####   IMPORTAMOS LA CLASE
from apps.administracion.views import Empleado_list,Empleado_crear,Empleado_editar,Emplado_eliminar

from apps.administracion.views import Area_list,Area_crear, Area_editar,Area_eliminar

from apps.administracion.views import Propietario_list,Propietario_crear,Propietario_editar,Propietario_eliminar

from apps.administracion.views import  Reserva_list,Reserva_crear,Reserva_editar,Reserva_eliminar

from apps.administracion.views import visita_list,visita_crear,visita_editar,visita_eliminar, index

from django.contrib.auth.decorators import login_required







urlpatterns = [


## url para mostrar los registros basada en clases
url(r'^listar$', login_required( Empleado_list.as_view()), name='empleado_listar'),



url(r'^nuevo$', login_required( Empleado_crear.as_view()), name='empleado_crear'),



url(r'^editar/(?P<pk>\d+)/$',login_required (Empleado_editar.as_view()), name='empleado_editar'),



url(r'^eliminar/(?P<pk>\d+)/$', login_required( Emplado_eliminar.as_view()), name='empleado_eliminar'),




###################################################
#####################  AREA  ######################

url(r'^listarArea$',login_required(Area_list.as_view()), name='area_listar'),


url(r'^nuevoArea$', login_required(Area_crear.as_view()), name='area_crear'),


url(r'^editarArea/(?P<pk>\d+)/$',login_required(Area_editar.as_view()), name='area_editar'),


url(r'^eliminarArea/(?P<pk>\d+)/$',login_required(Area_eliminar.as_view()), name='area_eliminar'),


##############################################
    ########### RESERVA  #####################

url(r'^listarReserva$',login_required(Reserva_list.as_view()), name='reserva_listar'),

url(r'^nuevoReserva$',  login_required(Reserva_crear.as_view()), name='reserva_crear'),


url(r'^editarReserva/(?P<pk>\d+)/$',login_required(Reserva_editar.as_view()), name='reserva_editar'),


url(r'^eliminarReserva/(?P<pk>\d+)/$',login_required(Reserva_eliminar.as_view()), name='reserva_eliminar'),



###################################################
###################  PROPIETARIO  ######################

url(r'^listarPropietario$', login_required(Propietario_list.as_view()), name='propietario_listar'),


url(r'^nuevoPropietario$',  login_required(Propietario_crear.as_view()), name='propietario_crear'),


url(r'^editarPropietario/(?P<pk>\d+)/$', login_required(Propietario_editar.as_view()), name='propietario_editar'),


url(r'^eliminarPropietario/(?P<pk>\d+)/$',  login_required(Propietario_eliminar.as_view()), name='propietario_eliminar'),







## url para mostrar los registros basada en clases
url(r'^visitaListar$', login_required(visita_list.as_view()), name='visita_listar'),



url(r'^visitaNuevo$',  login_required(visita_crear.as_view()), name='visita_crear'),



url(r'^visitaEditar/(?P<pk>\d+)/$',login_required(visita_editar.as_view()), name='visita_editar'),



url(r'^visitaEliminar/(?P<pk>\d+)/$', login_required(visita_eliminar.as_view()), name='visita_eliminar'),



###########################################################
##############  ##PAGINA PRINCIPAL  #######################

url(r'^principal$',login_required(index), name='index'),


###########################################################
url(r'^registrar$', index, name='registrar'),




]