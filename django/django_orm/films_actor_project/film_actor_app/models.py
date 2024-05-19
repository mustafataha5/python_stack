from django.db import models

# Create your models here.


class Actor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Category(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Language(models.Model):
    name =models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
            
class Movie(models.Model): 
    title = models.CharField(max_length=255)
    description = models.TextField()
    image_url = models.TextField()
    actors = models.ManyToManyField(Actor,related_name="movies")
    categories = models.ManyToManyField(Category,related_name="movies")
    language = models.ForeignKey(Language,related_name="movies",on_delete=models.CASCADE)
    release_year = models.DateField()
    duration = models.IntegerField()
    rental_rate = models.DecimalField(default=4.99,max_digits=3, decimal_places=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    


  





