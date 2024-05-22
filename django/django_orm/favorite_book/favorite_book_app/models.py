from django.db import models

# Create your models here.

import re 
import bcrypt
import datetime
# Create your models here.


class UserManager(models.Manager):
    def basic_validation(self,postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        
        if len(postData['first_name']) < 2 :
            errors['first_name'] = "First name should be a least 2 characters ."
        if len(postData['last_name']) < 2 :
            errors['last_name'] = "Last name should be a least 2 characters ."   
        if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern            
            errors['email'] = "Invalid email address!"
        elif len(User.objects.filter(email=postData['email'])) > 0 : 
            errors['email'] = "Used email address "
            
        if len(postData['password']) <8: 
             errors['password'] = 'Password must be at least  8 characters .'
        if postData['password'] != postData['confirm_password'] : 
            errors['confirm_password'] = 'Does not match password .'   
        if datetime.datetime.strptime(postData['birthday'],'%Y-%m-%d').date() > datetime.date.today() :
            errors['birthday'] ='Birthday must be in past.'
        days =  abs(datetime.datetime.strptime(postData['birthday'],'%Y-%m-%d').date()-datetime.date.today())   
        if  days.days < 13*365:
            errors['birthday'] ='You must be at least 13 old year.'   
            
        return errors
    
    def login_validation(self,postData): 
        errors= {}
        
        if len(User.objects.filter(email=postData['email'])) == 0 : 
            errors['login_email'] = "Wrong email address "
            errors['login_password'] = "Wrong password"
        else: 
            user = User.objects.get(email=postData['email'])
            if not bcrypt.checkpw(postData['password'].encode(),user.password.encode()) : 
                errors['login_password'] = "Wrong password"
        return errors        
    
class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=127)
    password = models.CharField(max_length=50)
    birthday = models.DateField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    
    
    
class BookManager(models.Manager):
    def book_validation(self,postData):
        errors= {}
        if len(postData['title']) < 5 : 
            errors['book_title'] = 'Title must be at least 5 charcter'    
        return errors
        
class Book(models.Model):    
    title = models.CharField(max_length=255)
    desc = models.TextField()
    uploaded_by = models.ForeignKey(User,related_name="books_uploaded",on_delete=models.CASCADE)
    users_who_like = models.ManyToManyField(User,related_name="liked_books")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()         
        
        
