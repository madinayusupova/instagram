from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class UserFollowing(models.Model):
    user_id = models.ForeignKey(User, related_name="following", on_delete=models.DO_NOTHING)
    following_user_id = models.ForeignKey(User, related_name="followers", on_delete=models.DO_NOTHING)
    created = models.DateTimeField(auto_now_add=True)


