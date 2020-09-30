from django.db import models
from django.contrib.auth import get_user_model
UserModel = get_user_model()

# Create your models here.

class UserFollowing(models.Model):
    user_to = models.ForeignKey(UserModel, related_name="following", on_delete=models.CASCADE)
    following_user_id = models.ForeignKey(UserModel, related_name="followers", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        unique_together = ("user_to", "following_user_id")
        ordering = ["-created"]

    def __str__(self):
        f"{self.user_to} follows {self.following_user_id}"