
# NOTA :: Esta es la clase para el formulario que  para que se muestre en pantalla
#         Este formulario esta referenciado por un vista.
from django import forms

from apps.administracion.models import Empleado

from apps.administracion.models import Area

from apps.administracion.models import Propietario


from apps.administracion.models import Reserva

from apps.administracion.models import Visita


class EmpleadoForm(forms.ModelForm):

	class Meta:
		model = Empleado

		fields = [
			'nombre',
			'apellidos',
			'cedula',
			'cargo',
		]
		labels = {
			'nombre': 'Nombre',
			'apellidos': 'apellidos',
			'cedula': 'cedula',
			'cargo':'cargo',
		}
		widgets = {
			'nombre': forms.TextInput(attrs={'class':'form-control'}),
			'apellidos': forms.TextInput(attrs={'class':'form-control'}),
			'cedula': forms.NumberInput(attrs={'class':'form-control'}),
			'cargo': forms.Select(attrs={'class': 'form-control'}),
		}










class AreaForm1(forms.ModelForm):
	class Meta:
		model = Area

		fields = [
			'seccion',
			'nombre',
			'sector',
			'horaHora',
			'horaMinutos',
			'descripcion',
			'estado',
			'tiempoVisitaTiempo',
			'tiempoHoras'
		]
		labels = {
			'seccion':'Seccion',
			'nombre':'Nombre',
			'sector':'Sector',
			'horaHora':'Desde (Hrs.)',
			'horaMinutos':'Hasta (Hrs.)',
			'descripcion':'Descripcion',
			'estado':'Estado',
			'tiempoVisitaTiempo':'Tiempo',
			'tiempoHoras':'Horas'

		}
		widgets = {
			'seccion': forms.Select(attrs={'class': 'form-control'}),
			'nombre': forms.TextInput(attrs={'class': 'form-control'}),
			'sector': forms.Select(attrs={'class': 'form-control'}),
			'horaHora': forms.Select(attrs={'class': 'form-control'}),
			'horaMinutos': forms.Select(attrs={'class': 'form-control'}),
			'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
			'estado': forms.Select(attrs={'class': 'form-control'}),
			'tiempoVisitaTiempo': forms.Select(attrs={'class': 'form-control'}),
			'tiempoHoras': forms.Select(attrs={'class': 'form-control'}),


		}






class PropietarioForm(forms.ModelForm):

	class Meta:
		model = Propietario

		fields = [
			'nombre',
			'apellidos',
			'cedula',
			'numero_casa',
		]
		labels = {
			'nombre': 'nombre',
			'apellidos': 'apellidos',
			'cedula': 'cedula',
			'numero_casa':'numero_casa',
		}
		widgets = {
			'nombre': forms.TextInput(attrs={'class':'form-control'}),
			'apellidos': forms.TextInput(attrs={'class':'form-control'}),
			'cedula': forms.NumberInput(attrs={'class':'form-control'}),
			'numero_casa': forms.NumberInput(attrs={'class':'form-control'}),
		}





class ReservaForm(forms.ModelForm):

	class Meta:
		model =  Reserva

		fields = [

			'propietario',
			'area',
			'fecha',
			'desdeHora',
			'hastaHora',
			'empleado',
		]
		labels = {

			'propietario': 'propietario',
			'area': 'area',
			'fecha':'fecha',
		    'desdeHora':'desdeHora',
			'hastaHora':'hastaHora',
			'empleado':'empleado',
		}
		widgets = {

			'propietario': forms.Select(attrs={'class':'form-control'}),
			'area': forms.Select(attrs={'class':'form-control'}),
			'fecha': forms.DateInput(attrs={'class':'form-control', 'id':'Date2', 'data-date-format':'dd/mm/yyyy'}),

			'desdeHora': forms.Select(attrs={'class': 'form-control'}),
			'hastaHora': forms.Select(attrs={'class': 'form-control'}),

			'empleado': forms.Select(attrs={'class':'form-control'}),
		}











class VisitaForm(forms.ModelForm):

	class Meta:
		model = Visita

		fields = [
			'cedula',
			'nombre',
			'apellidos',
			'observacion',
			'fechaEntrada',
			'fechaSalida',
			'tiempoVisitaTiempo',
			'tiempoHoras',
			'modoEntrada',

			'propietario'

		]
		labels = {
			'cedula': 'CI',
			'nombre': 'Nombres',
			'apellidos': 'Apellidos',
			'observacion':'Observacion',
			'fechaEntrada':'Fecha Entrada',
			'fechaSalida':'Fecha Salida',
			'tiempoVisitaTiempo':'Tiempo',
			'tiempoHoras':'Formato',
			'modoEntrada':'Modo de Entrada',
			'Propietario': 'Propietarios',

		}
		widgets = {
			'cedula':forms.NumberInput(attrs={'class':'form-control'}),
			'nombre': forms.TextInput(attrs={'class':'form-control'}),
			'apellidos': forms.TextInput(attrs={'class':'form-control'}),
			'observacion':forms.Textarea(attrs={'class':'form-control'}),
			'fechaEntrada': forms.DateInput(attrs={'class':'form-control', 'id':'Date', 'data-date-format':'dd/mm/yyyy'}),
			'fechaSalida':  forms.DateInput(attrs={'class':'form-control', 'id':'Date1', 'data-date-format':'dd/mm/yyyy'}),
			'tiempoVisitaTiempo':forms.Select(attrs={'class':'form-control'}),
			'tiempoHoras':forms.Select(attrs={'class': 'form-control'}),
			'modoEntrada':forms.Select(attrs={'class':'form-control'}),
			'propietario': forms.Select(attrs={'class': 'form-control'}),
		}

	#	'estado': forms.Select(attrs={'class': 'form-control'}),