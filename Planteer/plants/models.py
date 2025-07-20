from django.db import models

# Create your models here.
class Plants(models.Model):

    class CategoryChoices(models.TextChoices):
        TREE = 'tree', 'Tree'
        VEGETABLE = 'vegetable', 'Vegetable'
        FRUIT = 'fruit', 'Fruit'
        HERB_SPICE = 'herb_spice', 'Herbs & Spices'
        FLOWER_ORNAMENTAL = 'flower_ornamental', 'Flowers & Ornamentals'
        SUCCULENT_INDOOR = 'succulent_indoor', 'Succulents & Indoor'

    name = models.CharField(max_length=1024)
    about = models.TextField()
    used_for = models.TextField()
    image = models.ImageField(upload_to="images/", default="images/default.png")
    category = models.CharField(max_length=32,choices=CategoryChoices.choices)
    is_edible = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    plant = models.ForeignKey(Plants, on_delete= models.CASCADE)
    full_name = models.CharField(max_length=1024)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)