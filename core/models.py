from django.db import models


class Curso(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    carga_horaria = models.IntegerField()
    imagem = models.ImageField(upload_to='cursos/', null=True, blank=True)

    def __str__(self):
        return self.nome


class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    imagem = models.ImageField(upload_to='noticias/', null=True, blank=True)
    data_publicacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo


class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20)
    data_nascimento = models.DateField()
    foto = models.ImageField(upload_to='alunos/', null=True, blank=True)
    curso = models.ManyToManyField(Curso, blank=True)

    def __str__(self):
        return self.nome


class Contato(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    mensagem = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} ({self.email})"