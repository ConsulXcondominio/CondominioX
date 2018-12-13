from django.conf.urls import url

from apps.usuario.views import RegistroUsuario,Registro_list,Registro_editar,Registro_eliminar

from django.contrib.auth.decorators import login_required

urlpatterns = [

	url(r'^listarUsuario',Registro_list.as_view(), name="usuario_listar"),

	url(r'^registrarUsuario',RegistroUsuario.as_view(), name="usuraio_crear"),

	url(r'^editarUsuario/(?P<pk>\d+)/$',login_required (Registro_editar.as_view()), name='usuario_editar'),

	url(r'^eliminarUsuario/(?P<pk>\d+)/$',login_required (Registro_eliminar.as_view()), name='usuario_eliminar'),


]