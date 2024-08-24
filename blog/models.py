from django.db import models

class Habilidades_tecnicas(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    
    def __str__(self):
        return self.nome

class Atividades_extra(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    
    def __str__(self):
        return self.nome

class Pessoal(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=100)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='images/', blank=True)
    video = models.FileField(upload_to='videos/', blank=True)
    
    def __str__(self):
        return self.titulo