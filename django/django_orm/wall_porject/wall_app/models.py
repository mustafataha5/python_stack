from django.db import models
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
    
class MeassageManger(models.Manager):
    def post_validation(self,postData):
        errors ={}
       # print("*"*80,postData)
        if len(postData['post_message']) ==0 :
            errors['error_post_message'] = 'Please fill the Post message field'
        return errors 
    def can_delete(self,postID): 
        post = Message.objects.get(id=postID)
        pass_time =  abs(post.updated_at.timestamp() - datetime.datetime.timestamp(datetime.datetime.today())) 
        print("Pass ->>>>>>>>>>>>>>>>. ********",pass_time )
        print(pass_time < 30*60)
        return pass_time < 30*60 # 30 min 
 
          

class Message(models.Model):
    message = models.TextField()
    user = models.ForeignKey(User,related_name='messages',on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = MeassageManger()
    
class CommentManager(models.Manager):
    def comment_validation(self,postData,postID,userID): 
        errors ={}
        if len(postData['comment_message']) == 0 :
            errors['comment_message-'+str(userID)+str(postID)] = 'Please fill the comment message field'
        
        return errors    
class Comment(models.Model):    
    comment_message = models.TextField(default="")
    user = models.ForeignKey(User,related_name='comments',on_delete=models.CASCADE)
    message = models.ForeignKey(Message,related_name='comments',on_delete=models.CASCADE)
    objects = CommentManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)