from django.db import models

# Create your models here.

class Plant(models.Model):

    class CategoryChoices(models.TextChoices):
        TREE = 'Tree', 'Tree'
        HERB = 'Herb', 'Herb'
        FLOWER = 'Flower', 'Flower'
        FRUIT = 'Fruit', 'Fruit'
        VEGETABLE = 'Vegetable', 'Vegetable'
        SUCCULENT = 'Succulent', 'Succulent'

    name = models.CharField(max_length=100)
    about = models.TextField()
    used_for = models.TextField()
    image = models.ImageField(upload_to="images/")
    category = models.CharField(max_length=20, choices=CategoryChoices.choices, default= CategoryChoices.TREE)
    is_edible = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=1024)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)