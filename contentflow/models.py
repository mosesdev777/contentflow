from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.db.models.signals import post_save
# Create your models here.

class Profile(models.Model):
    
    def get_absolute_url(self):
        return f'/users/{self.user.username}'
    
    user = models. OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=get_absolute_url, blank=True, null=True)
    rol = models.CharField(max_length=200,null=False, blank=False)
    
    def create_profile(self, created, sender, instance, **kwargs):
        if created:
            profile = Profile.objects.create(user=instance)
            profile.save()
    post_save.connect(receiver=create_profile, sender=User)
    
    def __str__(self):
        return self.user.username    
    
        

class Publication(models.Model):
    
    VOICE_CHOICES = (
        ('Human', 'Human'),
        ('AI', 'AI'),
    )
    
    STATUS_CHOICES = (
        ('Created', 'Created'),
        ('Published', 'Published'),
        ('Deleted', 'Deleted'),
    )
    FORMAT_CHOICES = (
        ('Long Video', 'Long Video'),
        ('Post', 'Post'),
        ('Short', 'Short'),
        ('Reel', 'Short'),
        ('Story', 'Story'),
    )
    
    
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=False, null=False)
    slug = models.SlugField(unique=True, null=True, blank=True)
    description = models.TextField(blank=False, null=False)
    script = models.TextField(blank=False, null=False)
    thumbnail_title = models.TextField(blank=True, null=True)
    voice_type = models.CharField(max_length=100, choices=VOICE_CHOICES, default='Human', null=False, blank=False)
    voice_author = models.ForeignKey('VoiceAuthor', null=True, blank=True, on_delete=models.CASCADE)
    voice_name = models.CharField(max_length=100, null=False, blank=True)
    status = models.CharField(max_length=100, null=False, blank=False, choices=STATUS_CHOICES)
    content_format =  models.CharField(max_length=100, null=False, blank=True, choices=FORMAT_CHOICES, default='Post')
    background_music = models.CharField(max_length=200, blank=True, null=True)
    social_media = models.ManyToManyField('SocialMedia')

    #Timestamps
    created_at = models.DateTimeField(auto_now_add=True)    
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(auto_now=True)
    
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        
    def __str__(self):
        return self.title    
    

class SocialMedia(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    icon = models.ImageField(upload_to='social/image')
    url = models.URLField(max_length=200)
    
    created_at =  models.DateTimeField(auto_now_add=True)
    upadated_at =  models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name


class VoiceAuthor(models.Model):
    name = models.CharField(max_length=100,null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)    
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
