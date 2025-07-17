from django.db import models

# Create your models here.


class Plant(models.Model):
    
    class PlantCategory(models.TextChoices):
        DECORATIVE = 'decorative', 'Decorative Plants'
        INDOOR = 'indoor', 'Indoor Plants'
        OUTDOOR = 'outdoor', 'Outdoor Plants'
        FLOWERING = 'flowering', 'Flowering Plants'
        MEDICINAL = 'medicinal', 'Medicinal Plants'
        AROMATIC = 'aromatic', 'Aromatic Plants'
        EDIBLE = 'edible', 'Edible Plants'
        CLIMBING = 'climbing', 'Climbing Plants'
        SUCCULENT = 'succulent', 'Succulent Plants'
        RARE = 'rare', 'Rare Plants'
        AIR = 'air', 'Air Plants'
        AQUATIC = 'aquatic', 'Aquatic Plants'
        CARNIVOROUS = 'carnivorous', 'Carnivorous Plants'
        PERENNIAL = 'perennial', 'Perennial Plants'
        SEASONAL = 'seasonal', 'Seasonal Plants'
    
    name = models.CharField(max_length=255)
    about = models.TextField()
    used_for = models.TextField()
    image = models.ImageField(upload_to='images/')
    category = models.CharField(choices=PlantCategory.choices)
    is_edible = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    
class Comment(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
