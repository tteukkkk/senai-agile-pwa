from django.test import TestCase

from popular_banco import popular_banco
from .models import Aluno, Contato, Curso, Noticia


class PopularBancoTests(TestCase):
    def test_popular_banco_cria_registros_para_o_site(self):
        popular_banco()

        self.assertGreater(Curso.objects.count(), 0)
        self.assertGreater(Noticia.objects.count(), 0)
        self.assertGreater(Aluno.objects.count(), 0)
        self.assertGreater(Contato.objects.count(), 0)
        self.assertTrue(Curso.objects.filter(nome='Eletricista Industrial').exists())
        self.assertTrue(Aluno.objects.filter(nome='Aluno Demonstração 01').exists())
