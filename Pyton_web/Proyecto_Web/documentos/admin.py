# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from documentos.models import Documento


#crear subclase de admin.models

class DocumentoAdmin(admin.ModelAdmin):
	model = Documento

#registrar modeladmin para cada modelo

admin.site.register(Documento,DocumentoAdmin)