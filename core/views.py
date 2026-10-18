from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Noticia, Curso, Aluno, Contato
from .forms import AlunoForm, ContatoForm

# 1. Página de notícias
def noticias(request):
    noticias = Noticia.objects.all().order_by('-data_publicacao')
    return render(request, './core/noticias.html', {'noticias': noticias})

# 2. Página de cursos
def cursos(request):
    cursos = Curso.objects.all()
    return render(request, './core/cursos.html', {'cursos': cursos})

# 3. Cadastro de aluno (perfil)
def cadastro_aluno(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST, request.FILES)
        if form.is_valid():
            aluno = form.save()
            messages.success(request, "Perfil cadastrado com sucesso!")
            return redirect('perfil_aluno', aluno_id=aluno.id)
    else:
        form = AlunoForm()
    return render(request, './core/cadastro_aluno.html', {'form': form})

# 4. Matrícula em cursos
def matricula(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    alunos = Aluno.objects.all()
    if request.method == 'POST':
        aluno_id = request.POST.get('aluno_id')
        aluno = get_object_or_404(Aluno, id=aluno_id)
        aluno.curso.add(curso)
        messages.success(request, f"Matrícula realizada no curso '{curso.nome}' para o aluno '{aluno.nome}'.")
        return render(request, './core/success.html', {'mensagem': f"Você se matriculou com sucesso em {curso.nome}!"})
    
    return render(request, './core/matricula.html', {'curso': curso, 'alunos': alunos})

# 5. Formulário de contato
def contato(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Mensagem enviada com sucesso!")
            return render(request, './core/success.html', {'mensagem': "Obrigado pelo contato! Em breve retornaremos."})
    else:
        form = ContatoForm()
    return render(request, './core/contato.html', {'form': form})

# 6. Página de localização
def localizacao(request):
    return render(request, './core/localizacao.html')

# 7. Perfil do Aluno
def perfil_aluno(request, aluno_id):
    aluno = get_object_or_404(Aluno, id=aluno_id)
    return render(request, './core/perfil_aluno.html', {'aluno': aluno})

# 8. Lista de Alunos
def lista_alunos(request):
    alunos = Aluno.objects.all().order_by('nome')
    return render(request, './core/alunos.html', {'alunos': alunos})
