from django.db import models

# Create your models here.
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    place = models.CharField(max_length=50, null=True, blank=True)
    category = models.CharField(max_length=50)
    description = models.CharField(max_length=500000, null=True, blank=True)

