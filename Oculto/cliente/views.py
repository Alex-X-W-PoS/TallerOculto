# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from cliente.forms import Form1, Form2

# Create your views here.

def index (request):
	form = Form1()
	return render (request,'CamposOcultos/index.html',{'form':form})


def controlador1 (request):
	form = Form1(request.POST)
	if form.is_valid():
		print(request.POST)
		usuario = form.cleaned_data['usuario']
		password = form.cleaned_data['password']
		form2 = Form2(initial={'usuario': usuario,'password': password})
		return render (request,'CamposOcultos/secundaria.html',{'form': form2})

def controlador2 (request):
	form = Form2(request.POST)
	if form.is_valid():
		usuario = form.cleaned_data['usuario']
		password = form.cleaned_data['password']
		valor1 = form.cleaned_data['valor1']
		valor2 = form.cleaned_data['valor2']
		resultado = valor1 + valor2
		data = {'usuario': usuario, 'pass': password, 'valor1': valor1, 'valor2':valor2,'resultado':resultado}
		return render (request,'CamposOcultos/final.html',{'data': data})
	else:
		print(request.POST)
