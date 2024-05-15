from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=255)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

class Books(models.Model):
    title = models.CharField(max_length=255) 
    author_id = models.ForeignKey(Author,related_name="books",on_delete=models.CASCADE)  
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
   