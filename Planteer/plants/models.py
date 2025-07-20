from django.db import models

# Create your models here.

class Plant(models.Model):
    class CategoryChoices(models.TextChoices):
        DEFAULT = 'plant', 'plant'
        CATEGORY01 = 'FRUIT', 'Fruit'
        CATEGORY02 = 'VEGETABLE', 'Vegetable'
        CATEGORY03 = 'FLOWER', 'Flower'
        CATEGORY04 = 'HERB', 'Herb'
        CATEGORY05 = 'TREE', 'Tree'


    name = models.CharField(max_length=255)
    about = models.TextField()
    used_for = models.TextField()
    image = models.ImageField(upload_to='images/', default='images/default.jpg')
    category = models.CharField(max_length=50, choices=CategoryChoices.choices, default=CategoryChoices.DEFAULT)
    is_edible = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)