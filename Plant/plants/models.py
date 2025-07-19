from django.db import models

# Create your models here.


class Plant(models.Model):
    CATEGORY_CHOICES = [
        ('tree', 'Tree'),
        ('flower', 'Flower'),
        ('herb', 'Herb'),
        ('succulent', 'Succulent'),
        ('shrub', 'Shrub'),
    ]
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='plants/')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    is_edible = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    native_to = models.CharField(max_length=255, blank=True, null=True)
    used_for = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
