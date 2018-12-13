from django.contrib import admin
from apps.administracion.models import Empleado
from apps.administracion.models import Area
from apps.administracion.models import Propietario
from apps.administracion.models import Visita

# Register your models here.
admin.site.register(Empleado)
admin.site.register(Area)
admin.site.register(Propietario)
admin.site.register(Visita)
