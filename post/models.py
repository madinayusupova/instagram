from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField()
    text = models.TextField(max_length=350)
    posted = models.DateTimeField(auto_now_add=True)





# Create your models here.
