from django.db import models

# Create your models here.

class Disease(models.Model):
    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    depart = models.CharField(max_length=255) #choices = []

class Symptom(models.Model):
    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

class Symp_Ill(models.Model):
    '''
    M to M relationship table
    '''
    Ill = models.ForeignKey(Disease, on_delete=models.DO_NOTHING, related_name='symps')
    Symp = models.ForeignKey(Symptom, on_delete=models.DO_NOTHING, related_name='ills')


