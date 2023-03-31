from django.db import models

# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=80)
    category = models.CharField(max_length=20)
    company = models.CharField(max_length=50)
    url = models.URLField(max_length=120)
    

