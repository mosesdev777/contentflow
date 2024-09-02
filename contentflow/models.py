from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.db.models.signals import post_save
# Create your models here.


class MediaPlatform(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    social_media = models.ForeignKey('SocialMedia', null=False, blank=False)
    is_active = models.BooleanField(default=True, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
   
class Profile(models.Model):
    
    def get_absolute_url(self):
        return f'users/{self.user.username}'
    
    ROL_CHOICES = (
        ('admin', 'admin'),
        ('user', 'user'),
    )
    
    user = models. OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='users/avatar/', blank=True, null=True)
    rol = models.CharField(max_length=200,null=False, blank=False, choices=ROL_CHOICES, default='user')
    
    print(user.get_cache_name)
    
    def create_profile(created, sender, instance, **kwargs):
        if created:
            profile = Profile.objects.create(user=instance)
            profile.save()
    post_save.connect(receiver=create_profile, sender=User)
    
    def __str__(self):
        return self.user.username    
    
    def save(self, *args, **kwargs):
        self.avatar= f'users/avatar/{self.user.username}/{self.avatar.file}'
        super().save(*args, **kwargs)
    
        

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
    thumbnail_title = models.CharField(max_length=200,blank=True, null=True)
    voice_type = models.CharField(max_length=100, choices=VOICE_CHOICES, default='Human', null=False, blank=False)
    voice_author = models.ForeignKey('VoiceAuthor', null=True, blank=True, on_delete=models.CASCADE)
    voice_name = models.CharField(max_length=100, null=False, blank=True)
    status = models.CharField(max_length=100, null=False, blank=False, choices=STATUS_CHOICES, default='Created')
    content_format =  models.CharField(max_length=100, null=False, blank=True, choices=FORMAT_CHOICES, default='Post')
    background_music = models.CharField(max_length=200, blank=True, null=True)
    social_media = models.ManyToManyField('SocialMedia')

    #Timestamps
    created_at = models.DateTimeField(auto_now_add=True)    
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(auto_now=True)
    
    
    def save(self, *args, **kwargs):
        
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.title    
    

class SocialMedia(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    icon = models.ImageField(upload_to='social-media/image')
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
#Models for ideas 

class Subcription(models.Model):
    
    RENEWAL_CHOICES = (
        ('Yearly', 'Yearly'),
        ('Monthly', 'Monthly'),
        ('Each 3 Months', 'Each 3 Months'),
        ('Pay as you go', 'Pay as you go')
    )
    
    platform = models.CharField(max_length=200, blank=False, null=False)
    plan = models.CharField(max_length=200, null=False, blank=False)
    amount = models.FloatField(null=False, blank=False, default=0)
    mail = models.EmailField(null=False, blank=False)
    start_date = models.DateField()
    renewal = models.CharField(max_length=200, blank=False, null=False, choices=RENEWAL_CHOICES, default='Monthly')
    is_active = models.BooleanField(blank=False, null=False, default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    

class Planning(models.Model):
    
    FRECUENCY_CHOICES = (
        ('Dayly', 'Dayly'),
        ('On Sunday', 'On Sunday'),
        ('On Saturday', 'On Saturday'),
        ('Three times a week', 'Three times a week')
        ('Every 2 weeks', 'Every 2 weeks')
    )
    
    youtube = models.ForeignKey(Account, related_name='youtube', null=True, blank=True, choices=FRECUENCY_CHOICES, default='Dayly')
    meta = models.ForeignKey(Account, related_name='meta', null=True, blank=True)
    instagram = models.ForeignKey(Account, related_name='instagram', null=True, blank=True, choices=FRECUENCY_CHOICES, default='Dayly')
    tiktok = models.ForeignKey(Account, related_name='tiktok', null=True, blank=True, choices=FRECUENCY_CHOICES, default='Dayly')
    web = models.ForeignKey(Account, related_name='web', null=True, blank=True, choices=FRECUENCY_CHOICES, default='Dayly')
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(null=False, blank=False, default=True)
    
class Account(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    email = models.EmailField(null=False, blank=False)
    purpose = models.CharField(max_length=300, blank=False, null=False)
    username = models.CharField(max_length=200, blank=False, null=False) 
    phone = models.CharField(max_length=20,blank=True, null=True)
    two_factor_authenticator = models.CharField(max_length=200, blank=True, null=True)    
    
class Prompt(models.Model):
    
    FORMAT_CHOICES = (
        ('Long Video', 'Long Video'),
        ('Post', 'Post'),
        ('Short', 'Short'),
        ('Reel', 'Short'),
        ('Story', 'Story'),
    )
    
    channel = models.CharField(max_length=200, blank=False, null=False)
    content_format = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.channel        
    