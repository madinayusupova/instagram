from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserFollowing(models.Model):
    kto = models.ForeignKey(User, related_name="following", on_delete=models.CASCADE)
    kogo_follow = models.ForeignKey(User, related_name="followers", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        unique_together = ("kto", "kogo_follow")
        ordering = ["-created"]

    def __str__(self):
        f"{self.kto} follows {self.kogo_follow}"