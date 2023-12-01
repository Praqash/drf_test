from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    Title = models.CharField(max_length= 200)
    Content = models.TextField()
    Author = models.ForeignKey(User, on_delete= callable)
    Created_at = models.DateField(auto_now_add= True)




