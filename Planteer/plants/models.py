from django.db import models

class Plants(models.Model):
    name = models.CharField(default="Plant")
    about = models.TextField(default="Soon!")
    used_for = models.TextField(default="Soon!")
    image = models.ImageField(upload_to='images/',default="images/default.jpg")
    category = models.CharField(default='Fruit')
    is_editable = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    plant = models.ForeignKey(Plants, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)