from django.db import models
from django.utils import timezone


class Portofolios(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    images = models.ImageField(upload_to='images')
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

# Create your models here.
