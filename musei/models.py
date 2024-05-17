from django.db import models

# Create your models here.
class Museo(models.Model):
    nome= models.CharField(max_length=50)
    citta= models.CharField(max_length=20)
    stato= models.CharField(max_length=20)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name="Museo"
        verbose_name_plural="Musei"
    
    
class Autore(models.Model):
    nome= models.CharField(max_length=20)
    cognome= models.CharField(max_length=20)
    annoNascita= models.CharField(max_length=4)
    annoMorte= models.CharField(max_length=4)
    biografia= models.TextField()

    def __str__(self):
        return self.nome + " " + self.cognome
    
    class Meta:
        verbose_name="Autore"
        verbose_name_plural="Autori"
    
class Opera(models.Model):
    img= models.ImageField(upload_to='images/')
    nomeOp= models.CharField(max_length=50)
    anno= models.CharField(max_length=4)
    tipo= models.CharField(max_length=10)
    materiale= models.CharField(max_length=30)
    autore= models.ForeignKey(Autore, on_delete=models.CASCADE, related_name="opere")
    museo= models.ForeignKey(Museo, on_delete=models.CASCADE, related_name="opere")

    def __str__(self):
        return self.nomeOp
    
    class Meta:
        verbose_name="Opera"
        verbose_name_plural="Opere"