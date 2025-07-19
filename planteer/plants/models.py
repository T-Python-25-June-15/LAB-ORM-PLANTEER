from django.db import models

class Plant(models.Model):
    try:
        category = (
            ('Flower', 'Flower'),
            ('Fruit', 'Fruit'),
            ('Tree', 'Tree')
        )
    except Exception as e:
        print(f"Error occurred while defining categories: {e}")

    name = models.CharField(max_length=255)
    about = models.TextField()
    used_for = models.TextField()
    image = models.ImageField(upload_to='media/')
    category = models.CharField(max_length=255, choices=category)
    is_edible = models.BooleanField(default=False)
    native_to = models.CharField(max_length=255, blank=True)
    usage = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Review(models.Model):
       plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='reviews')
       name = models.CharField(max_length=255)
       comment = models.TextField()
       created_at = models.DateTimeField(auto_now_add=True)
    