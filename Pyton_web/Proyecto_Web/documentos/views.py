# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import View
from documentos.models import Documento

from django.shortcuts import render

# Create your views here.

#definir metodo get

class Documentos(View):
	def get(self,request,*args, **kwargs):
		docs = Documento.objects.all()
		#SELECT * FROM documentos_documentos; 
		context = {
		'docs':docs,
		'encabezado':'Mis Documentos'
		}
		return render(
			request,
			'documentos.html',
			context)