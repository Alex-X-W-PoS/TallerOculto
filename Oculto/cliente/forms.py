from django import forms

class Form1 (forms.Form):
	usuario = forms.CharField(max_length=50)
	password = forms.CharField(max_length=50)

class Form2 (forms.Form):
	valor1 = forms.IntegerField()
	valor2 = forms.IntegerField()
	usuario = forms.CharField(max_length=50)
	password = forms.CharField(max_length=50)
