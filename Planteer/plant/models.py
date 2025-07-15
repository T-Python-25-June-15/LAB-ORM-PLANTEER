from django.db import models

# Create your models here.

class Plant(models.Model):

    class CategoryChoices(models.TextChoices):
        TREE = 'Tree', 'Tree'
        SHRUB = 'Shrub', 'Shrub'
        HERB = 'Herb', 'Herb'
        VINE = 'Vine', 'Vine'
        FLOWER = 'Flower', 'Flower'
        FRUIT = 'Fruit', 'Fruit'
        VEGETABLE = 'Vegetable', 'Vegetable'
        SUCCULENT = 'Succulent', 'Succulent'

    name = models.CharField(max_length=100)
    about = models.TextField()
    used_for = models.TextField()
    image = models.ImageField(upload_to="images/", default="images/default.jpg")
    category = models.CharField(max_length=20, choices=CategoryChoices.choices, default= CategoryChoices.TREE)
    is_edible = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)