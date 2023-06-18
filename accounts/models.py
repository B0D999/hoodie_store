from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255, default='None')
    address = models.CharField(max_length=255, default='None')
    picture = models.ImageField(upload_to='profile_pictures', default='None')

    def __str__(self):
        return self.user.username
