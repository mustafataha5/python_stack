from django.db import models
import datetime
# Create your models here.



class ShowManager(models.Manager):
    def basic_validation(self,postData): 
        errors ={}
        if len(postData['title']) < 5 : 
            errors['title'] = "Error:  Title must be greater than 5 charcaters"
        if len(postData['network']) < 2 :
              errors['network'] = "Error:  Network must be greater than 2 charcater"
        try:
            datetime.date.fromisoformat( postData['release_date']) 
        except:    
            errors['release_date'] = f"Error: {postData['release_date']} is not valid Date "  
        # if postData['release_date'] < datetime.date('1910-01-01'): 
        #      errors['release_date'] += "Error:  Release date must be greater than 1910-01-01"
        # if postData['release_date'] > datetime.date.today(): 
        #      errors['release_date'] += "Error:  Release date must be less than future date"          
        if  len(postData['description']) < 10  : 
             errors['description'] = "Error:  Description must be greater than 10 charcaters"              
        
        return errors


class Show(models.Model):
    title = models.CharField(max_length=80)
    network = models.CharField(max_length=45)
    release_date = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects =ShowManager()
    
