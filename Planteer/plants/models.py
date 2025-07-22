from django.db import models

# Create your models here.

class Plant(models.Model):

    class CategoryChoices(models.TextChoices):
        HERB = 'Herb', 'Herb'
        SHRUB = 'fruit', 'Fruit'
        VEGETABLE = 'Vegetables', 'Vegetables'
        TREE = 'Tree', 'Tree'
        FLOWER = 'Flower', 'Flower'
        OTHER = 'Other', 'Other'

    name = models.CharField(max_length=255)
    about = models.TextField()
    used_for = models.TextField()
    image = models.ImageField(upload_to="images/", default="images/default.jpg")
    category = models.CharField(max_length=50, choices=CategoryChoices.choices)
    is_edible = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    

class Comment(models.Model):
    plant       = models.ForeignKey(Plant, on_delete=models.CASCADE)
    full_name   = models.CharField(max_length=255)
    content     = models.TextField(max_length=1024)
    created_at  = models.DateTimeField(auto_now_add=True)
