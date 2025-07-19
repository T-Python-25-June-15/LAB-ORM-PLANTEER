from django.db import models


class Plant(models.Model):

    class CategoryChoices(models.TextChoices):
        TYPE1 = "Flowering plants", "Flowering plants"
        TYPE2 = "Ferns and Mosses", "Ferns and Mosses"
        TYPE3 = "Algae", "Algae"
        TYPE4 = "Fungi", "Fungi"

    name = models.CharField(max_length=1024)
    about = models.TextField()
    used_for = models.TextField()
    image = models.ImageField(upload_to="images/", default="images/default.JPG")
    category = models.CharField(max_length=50, choices=CategoryChoices.choices)
    is_edible = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    plant = models.ForeignKey('Plant', on_delete=models.CASCADE)
    name = models.CharField(max_length=1024)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)



