from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Aluno,Curso

class PortalTests(TestCase):
    def test_matricula_relaciona_aluno_ao_curso(self):
        curso=Curso.objects.create(nome='Curso demo',descricao='Demo',carga_horaria=20)
        aluno=Aluno.objects.create(nome='Pessoa Demo',email='demo@example.com',telefone='00000000000',data_nascimento='2000-01-01')
        self.assertEqual(self.client.post(reverse('matricula',args=[curso.pk]),{'aluno_id':aluno.pk}).status_code,200)
        self.assertTrue(aluno.curso.filter(pk=curso.pk).exists())

    def test_service_worker_servido_na_raiz(self):
        response=self.client.get('/service-worker.js')
        self.assertEqual(response.status_code,200)
        self.assertEqual(response['Service-Worker-Allowed'],'/')
        response.close()

    def test_paginas_publicas(self):
        for name in ['noticias','cursos','lista_alunos','contato','localizacao']:
            with self.subTest(name=name):self.assertEqual(self.client.get(reverse(name)).status_code,200)
