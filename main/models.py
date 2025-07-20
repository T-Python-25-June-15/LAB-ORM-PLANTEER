from django.db import models
from django.utils import timezone

class PlantCategory(models.TextChoices):
    TREE = 'tree', 'Tree'
    FRUIT = 'fruit', 'Fruit'
    VEGETABLE = 'vegetable', 'Vegetable'

class Plants(models.Model):
    name = models.CharField(max_length=1024)
    about = models.TextField()
    used_for = models.TextField()
    image = models.ImageField(upload_to='images/', default='images/default.png')
    
    category = models.CharField(
        max_length=50,
        choices=PlantCategory.choices,
        default=PlantCategory.TREE
    )
    
    is_edible = models.BooleanField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Review(models.Model):
    plant = models.ForeignKey(Plants , on_delete=models.CASCADE)
    name = models.CharField(max_length=1024)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    

 