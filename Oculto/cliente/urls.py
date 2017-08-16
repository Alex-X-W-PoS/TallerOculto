from django.conf.urls import url, include
from django.contrib import admin
from cliente.views import index, controlador1, controlador2

urlpatterns = [
	url(r'^$', index, name='index'),
	url(r'^controlador1$', controlador1, name='controlador1'),
	url(r'^controlador2$', controlador2, name='controlador2'),
]
