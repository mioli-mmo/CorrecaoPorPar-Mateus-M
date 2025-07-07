from django.db import models

class Curso(models.Model):
    NIVEL = [
        (1, "Técnico"),
        (2, "Superior de Tecnologia"),
        (3, "Engenharia")
    ]
    nome = models.CharField(max_length=60)
    descricao = models.CharField(max_length=100)
    nivel = models.IntegerField(choices=NIVEL, default=1)
    def __str__(self):
        return self.nome

class Disciplina(models.Model):
    nome = models.CharField(max_length=40)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    def __str__(self):
        return self.nome
    