from django.db import models

# Create your models here.

class Plant(models.Model):
    class Category(models.TextChoices):
        HOUSEPLANT = 'Houseplant', 'Houseplant'
        HERB = 'Herb', 'Herb'
        TREE = 'Tree', 'Tree'

    name = models.CharField(max_length=150)
    about = models.TextField()
    used_for = models.TextField()
    image = models.ImageField(upload_to='plant_images/', default="images/default.jpg")
    category = models.CharField(max_length=20, choices=Category.choices)
    is_edible = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    
