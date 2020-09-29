from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from post.models import Post
from django.contrib.auth.models import User

    
class Comment(models.Model):
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name='comments')
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='comments', null= True)

    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('-created', )

    def str(self):
        return f"Comment by {self.author} on {self.post}"