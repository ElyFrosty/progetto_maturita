from django.db import models

# Create your models here.
class Museo(models.Model):
    nome= models.CharField(max_length=50)
    citta= models.CharField(max_length=20)
    stato= models.CharField(max_length=20)

    def __str__(self):
        return self.nome
    
    
class Autore(models.Model):
    nome= models.CharField(max_length=20)
    cognome= models.CharField(max_length=20)
    annoNascita= models.CharField(max_length=4)
    annoMorte= models.CharField(max_length=4)
    biografia= models.TextField()

    def __str__(self):
        return self.nome + " " + self.cognome
    
class Opera(models.Model):
    nomeOp= models.CharField(max_length=50)
    anno= models.CharField(max_length=4)
    tipo= models.CharField(max_length=10)
    materiale= models.CharField(max_length=30)
    autore= models.models.ForeignKey(Autore, on_delete=models.CASCADE, related_name="opere")

    def __str__(self):
        return self.nomeOp