from django.db import models

# Create your models here.

class Movies(models.Model):
    title = models.CharField(max_length=45)
    description = models.TextField()
    release_data = models.DateField()
    duration = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def __repe__(self):
    return f"{self.title}  {self.duration}"