from django.db import models

# Create your models here.
class Autor(models.Model):
    nome = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
 
    def __str__(self):
        return self.nome
 
class Post(models.Model):
    titulo = models.CharField(max_length=64)
    data = models.DateTimeField()
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    corpo = models.TextField()

    def __str__(self):
        return self.titulo



