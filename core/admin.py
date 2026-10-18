from django.contrib import admin
from .models import Curso, Noticia, Aluno, Contato

# Register your models here.

admin.site.register(Curso)
admin.site.register(Noticia)
admin.site.register(Aluno)
admin.site.register(Contato)