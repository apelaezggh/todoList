from django.db import models

# Create your models here.

class Activity(models.Model):
    name=models.CharField(max_length=50)
    contenido=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='activity'
        verbose_name_plural='activities'

    def __str__(self):
        return self.name 