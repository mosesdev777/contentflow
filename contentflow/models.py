from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models. OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='user/avatar', blank=True, null=True)
    rol = models.CharField(null=False, blank=False)

class SocialMedia(models.Model):
    pass

class Publication(models.Model):
    pass

class Thumbnail(models.Model):
    pass

class BackgroundMusic(models.Model):
    pass
