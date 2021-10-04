from django.db import models
from django.contrib.auth.models import User
from datetime import datetime,date
# Create your models here.

class Post(models.Model):

   title = models.CharField(max_length=250)
   author = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
   body = models.TextField()
   date = models.DateField(auto_now_add=True)
   likes = models.ManyToManyField(User,related_name='post_like')



   def total_likes(self):

      return self.likes.count()

   def __str__(self):

       return self.title + ' | '+ str(self.author)