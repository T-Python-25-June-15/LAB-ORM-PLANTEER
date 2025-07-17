from django.db import models

# Create your models here.


class Contact(models.Model):
    first_name = models.CharField()   
    last_name = models.CharField()   
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)   