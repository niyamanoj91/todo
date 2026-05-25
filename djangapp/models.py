from django.db import models

# Create your models here.
class djann(models.Model):
    course=models.CharField(max_length=100)
    fees=models.IntegerField()

    