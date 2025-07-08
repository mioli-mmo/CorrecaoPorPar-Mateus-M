from django.contrib import admin
from .models import Aluno, Avaliacao, Correcao, CorrecaoPorPar, Curso, Disciplina, Professor, Resposta, Turma

admin.site.register(Aluno)
admin.site.register(Avaliacao)
admin.site.register(Correcao)
admin.site.register(CorrecaoPorPar)
admin.site.register(Curso)
admin.site.register(Disciplina)
admin.site.register(Professor)
admin.site.register(Resposta)
admin.site.register(Turma)