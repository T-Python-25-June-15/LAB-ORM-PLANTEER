from django.db import models

class Plant(models.Model):

    category = (
        ('Flower', 'Flower'),
        ('Fruit', 'Fruit'),
        ('Tree', 'Tree')
    )

    name = models.CharField(max_length=255)
    about = models.TextField()
    used_for = models.TextField()
    image = models.ImageField(upload_to='media/')
    category = models.CharField(max_length=255, choices=category)
    is_edible = models.BooleanField(default=False)
    native_to = models.CharField(max_length=255, blank=True)
    usage = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
