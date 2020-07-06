from django.db import models

# Create your models here.

class Client(models.Model):
    nome = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    tel = models.CharField(max_length=25)
    adress = models.CharField(max_length=100)

    def __str__(self):
        return self.nome + " " + self.prenom

class Livraison(models.Model):
    libelle = models.CharField(max_length=100)
    date = models.DateTimeField()
    client = models.ForeignKey('Client', on_delete=models.CASCADE)
    #DATE_INPUT_FORMATS = ('%d-%m-%Y','%Y-%m-%d')
    #date_of_birth = DateField(input_formats=settings.DATE_INPUT_FORMATS)

    def __str__(self):
        return self.libelle