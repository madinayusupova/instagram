from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from post.models import Post
    
class Comment(models.Model):
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name='comments', blank=True, null=True)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='comments')

    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('-created', )

    def str(self):
        return f"Comment by {self.author} on {self.post}"