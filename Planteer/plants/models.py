from django.db import models

class Plant(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description = models.TextField()
    native_to = models.CharField(max_length=200)
    is_edible = models.BooleanField(default=False)
    usage = models.TextField()
    poster = models.ImageField(upload_to='images/', default='images/default.jpg')