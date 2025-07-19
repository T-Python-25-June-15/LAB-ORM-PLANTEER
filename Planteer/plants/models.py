from django.db import models

class Plant(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description = models.TextField()
    native_to = models.CharField(max_length=200)
    is_edible = models.BooleanField(default=False)
    usage = models.TextField()
    poster = models.ImageField(upload_to='images/', default='images/default.jpg')


class Comment (models.Model):
    plant = models.ForeignKey("Plant", on_delete=models.CASCADE, related_name="comments")
    full_name = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
            return f"Comment by {self.full_name} on {self.plant.title}"