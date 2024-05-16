from django.db import models

# Create your models here.


class Publisher(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Book(models.Model):
    title = models.CharField(max_length=255)
    publishers = models.ManyToManyField(Publisher,related_name='books')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    
