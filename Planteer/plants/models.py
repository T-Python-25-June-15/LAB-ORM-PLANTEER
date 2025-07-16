from django.db import models

# Create your models here.

class Plants(models.Model):
    class CategoryChoices(models.TextChoices):
        category1 = "Algae", "Algae"
        category2 = "Bryophytes", "Bryophytes"
        category3 = "Pteridophytes", "Pteridophytes"
        category4 = "Gymnosperms", "Gymnosperms"
        category5 = "Angiosperms", "Angiosperms" 
    name = models.CharField(max_length=1024)
    about = models.TextField()
    user_for = models.TextField()
    image = models.ImageField(upload_to="images/")
    category = models.CharField(choices=CategoryChoices.choices, default=CategoryChoices.category1)
    is_edible = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)