from django.db import models

# Create your models here.
class Plants(models.Model):
    name = models.CharField(default="Plant")
    about = models.TextField(default="Soon!")
    used_for = models.TextField(default="Soon!")
    image = models.ImageField(default="images/default.jpg")
    category = models.CharField(default='Fruit')
    is_editable = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
