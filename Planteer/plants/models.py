from django.db import models

class Plant(models.Model):


    class CategoriesChoices(models.TextChoices):
        TREE = 'TREE', 'Tree'
        FRUIT = 'FRUIT', 'Fruit'
        VEGETABLES = 'VEGETABLES', 'Vegetables'

    name= models.CharField(max_length=20)
    about = models.TextField()
    used_for=models.TextField()
    image = models.ImageField(upload_to="images/",default='images/default.jpg')
    category = models.CharField(choices=CategoriesChoices.choices,max_length=50)
    is_edible = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    full_name = models.CharField(max_length=24)
    content = models.TextField()
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='comments')

    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.full_name