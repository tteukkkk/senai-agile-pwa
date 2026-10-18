from django.urls import path
from . import views

urlpatterns = [
    path('', views.noticias, name='noticias'), # Página inicial: notícias
    path('cursos/', views.cursos, name='cursos'), # Lista de cursos
    path('cadastro/', views.cadastro_aluno, name='cadastro_aluno'), # Cadastro/Perfil aluno
    path('matricula/<int:curso_id>/', views.matricula, name='matricula'), # Matrícula em curso
    path('contato/', views.contato, name='contato'), # Contato
    path('localizacao/', views.localizacao, name='localizacao'), # Localização da escola
    path('alunos/', views.lista_alunos, name='lista_alunos'),
    path('perfil/<int:aluno_id>/', views.perfil_aluno, name='perfil_aluno'), # Perfil do aluno
]