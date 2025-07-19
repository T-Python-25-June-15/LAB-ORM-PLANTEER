from django.db import models
import datetime 
# Create your models here.
class Plant(models.Model):

    class CategoryChoices(models.TextChoices):
        CATEGORY1 = "Indoor", "Indoor"
        CATEGORY2 = "Outdoor", "Outdoor"
        CATEGORY3 = "Flowers", "Flowers"
        CATEGORY4 = "Herb", "Herb"
        CATEGORY5 = "Tree", "Tree"
        CATEGORY6 = "cactus", "cactus"
        
    name = models.CharField(max_length=1024)
    about = models.TextField()
    used_for = models.TextField()
    image = models.ImageField(upload_to="images/", default="images/default.jpg")
    category = models.CharField(max_length=1024, choices=CategoryChoices.choices)
    is_edible = models.BooleanField()
    created_at = models.DateField(auto_now_add=True)

class Comment(models.Model):
    plant = models.ForeignKey(Plant, on_delete= models.CASCADE)
    full_name = models.CharField(max_length=1024)
    plant_relation = models.TextField()
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)
