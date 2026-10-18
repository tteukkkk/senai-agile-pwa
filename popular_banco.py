"""Recria dados demonstrativos fictícios; use somente em banco local descartável."""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'senai_agile.settings')
django.setup()

from django.db import transaction
from core.models import Aluno, Contato, Curso, Noticia


@transaction.atomic
def popular_banco():
    """Apaga os registros do portal e insere apenas exemplos sintéticos."""
    Contato.objects.all().delete()
    Aluno.objects.all().delete()
    Noticia.objects.all().delete()
    Curso.objects.all().delete()
    curso = Curso.objects.create(nome='Eletricista Industrial', descricao='Curso fictício para demonstração local.', carga_horaria=160)
    Noticia.objects.create(titulo='Notícia de demonstração', conteudo='Conteúdo fictício para o portfólio acadêmico.')
    aluno = Aluno.objects.create(nome='Aluno Demonstração 01', email='aluno01@example.com', telefone='00000000000', data_nascimento='2000-01-01')
    aluno.curso.add(curso)
    Contato.objects.create(nome='Contato Demonstração 01', email='contato01@example.com', mensagem='Mensagem fictícia de demonstração.')
    print('Dados de demonstração sintéticos criados.')


if __name__ == '__main__':
    popular_banco()
