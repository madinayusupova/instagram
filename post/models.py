from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post_images/')
    text = models.TextField(max_length=350)
    posted = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title




# Create your models here.
