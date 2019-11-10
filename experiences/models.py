from django.db import models


# Create your models here.
class experiences(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.TextField()