from django.db import models
from django.utils import timezone
# Create your models here.

class Plant(models.Model):
    class PlantCategory(models.TextChoices):
        TREE = 'Tree'
        FRUIT = 'Fruit'
        VEGETABLE = 'Vegetables'
        HERB = 'Herb'
        OTHER = 'Other'

    name = models.CharField(max_length=255)
    about = models.TextField()
    used_for = models.TextField()
    image = models.ImageField(upload_to="plants/")
    category = models.CharField(max_length=50, choices=PlantCategory.choices)
    is_edible = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    
    
class Review(models.Model):
    plant = models.ForeignKey("Plant", on_delete=models.CASCADE, related_name="reviews")
    name = models.CharField(max_length=255)
    rating = models.SmallIntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.rating}"