from django.db import models

# Create your models here.
class Plant(models.Model):
    class Category(models.TextChoices):
        TREE = 'Tree'
        FRUIT = 'Fruit'
        VEGETABLE = 'Vegetables'
        HERB = 'Herb'

    name = models.CharField(max_length=200)
    about = models.TextField()
    used_for = models.TextField()
    image = models.ImageField(upload_to='plants/')
    category = models.CharField(max_length=20, choices=Category.choices)
    is_edible = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='comments')
    full_name = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

