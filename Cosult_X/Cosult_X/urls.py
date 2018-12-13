"""Cosult_X URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from django.contrib.auth.views import login, logout_then_login


urlpatterns = [
    url(r'^admin/', admin.site.urls),



#NOTA :: Cuando se realize una busqueda de archivos desde la pagina web buscara las urls establecidas aqui
#hace referencia a la url de la aplicaicon empleado urls.py

    url(r'^empleado/', include('apps.administracion.urls', namespace="empleado")),

    url(r'^visita/', include('apps.administracion.urls', namespace="visita")),

    url(r'^area/', include('apps.administracion.urls', namespace="area")),

    url(r'^propietario/', include('apps.administracion.urls', namespace="propietario")),


    url(r'^reserva/', include('apps.administracion.urls', namespace="reserva")),







     url(r'^usuario/', include('apps.usuario.urls', namespace="usuario")),

# esta es la url para que nos permite logearnos al sistmea (valida que se deve de estar logueado antes de ingresar el sistema)
    url(r'^accounts/login/', login, {'template_name':'index.html'}, name='login'),

#url que utilizamos para deslogearnos.
    url(r'^logout/', logout_then_login, name='logout'),

]
