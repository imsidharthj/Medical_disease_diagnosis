from django.db import models

class Disease(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Symptom(models.Model):
    disease = models.ForeignKey(Disease, related_name='symptoms', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
