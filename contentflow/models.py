from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.db.models.signals import post_save
# Create your models here.


class MediaPlatform(models.Model):
    """
    This model is used to register  avery channel or profile in wich you going to create content
    """
    name = models.CharField(max_length=200, blank=False, null=False)
    social_media = models.ForeignKey('SocialMedia', null=False, blank=False, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
   
class Profile(models.Model):
    
    def get_absolute_url(self):
        return f'users/{self.user.username}'
    
    ROL_CHOICES = (
        ('admin', 'admin'),
        ('user', 'user'),
    )
    
    user = models. OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    avatar = models.ImageField(upload_to='users/avatar/', blank=True, null=True)
    rol = models.CharField(max_length=200,null=False, blank=False, choices=ROL_CHOICES, default='user')
    
    
    def create_profile(created, sender, instance, **kwargs):
        if created:
            profile = Profile.objects.create(user=instance)
            profile.save()
    post_save.connect(receiver=create_profile, sender=User)
    
    def __str__(self):
        return self.user.username    
    
    """def save(self, *args, **kwargs):
        # Todo: rename the avatar image when uploaded
        #self.avatar= f'users/avatar/{self.user.username}/{self.avatar.file}'
        super().save(*args, **kwargs)
    """
        

class Publication(models.Model):
    
    VOICE_CHOICES = (
        ('h', 'Human'),
        ('ai', 'AI'),
    )
    
    STATUS_CHOICES = (
        ('c', 'Created'),
        ('p', 'Published'),
        ('d', 'Deleted'),
    )
    FORMAT_CHOICES = (
        ('l', 'Long Video'),
        ('p', 'Post'),
        ('s', 'Short'),
        ('r', 'Reel'),
        ('st', 'Story'),
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
    updated_at = models.DateField(auto_now=True)
    published_at = models.DateField(auto_now=True)
    
    
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
    updated_at = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.name
#Models for ideas 

class Subcription(models.Model):
    
    RENEWAL_CHOICES = (
        ('y', 'Yearly'),
        ('m', 'Monthly'),
        ('e3m', 'Each 3 Months'),
        ('pag', 'Pay as you go')
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
    
    def __str__(self):
        return self.platform
    
    

class Planning(models.Model):
    
    FRECUENCY_CHOICES = (
        ('d', 'Dayly'),
        ('su', 'On Sunday'),
        ('sa', 'On Saturday'),
        ('3tw', 'Three times a week'),
        ('e2w', 'Every 2 weeks')
    )
    
    youtube = models.ForeignKey('Account', related_name='youtube', null=True, blank=True, choices=FRECUENCY_CHOICES, default='Dayly', on_delete=models.CASCADE)
    meta = models.ForeignKey('Account', related_name='meta', null=True, blank=True, on_delete=models.CASCADE, choices=FRECUENCY_CHOICES)
    instagram = models.ForeignKey('Account', related_name='instagram', null=True, blank=True, choices=FRECUENCY_CHOICES, default='Dayly', on_delete=models.CASCADE)
    tiktok = models.ForeignKey('Account', related_name='tiktok', null=True, blank=True, choices=FRECUENCY_CHOICES, default='Dayly', on_delete=models.CASCADE)
    web = models.ForeignKey('Account', related_name='web', null=True, blank=True, choices=FRECUENCY_CHOICES, default='Dayly', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(null=False, blank=False, default=True)
    
    def __str__(self):
        return self.created_at
    
    
class Account(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    email = models.EmailField(null=False, blank=False)
    purpose = models.CharField(max_length=300, blank=False, null=False)
    username = models.CharField(max_length=200, blank=False, null=False) 
    phone = models.CharField(max_length=20,blank=True, null=True)
    two_factor_authenticator = models.CharField(max_length=200, blank=True, null=True)    
    
    def __str__(self):
        return self.name
    
class Prompt(models.Model):
    
    FORMAT_CHOICES = (
        ('l', 'Long Video'),
        ('p', 'Post'),
        ('s', 'Short'),
        ('r', 'Reel'),
        ('st', 'Story'),
    )
    
    channel = models.ForeignKey(MediaPlatform, on_delete=models.CASCADE, null=False, blank=False)
    content_format = models.CharField(max_length=200, null=False, blank=False, choices=FORMAT_CHOICES)
    text = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.channel        

class Title(models.Model):
    
    """
    This model is for having every title you are going to use to create content
    """
    FORMAT_CHOICES = (
        ('lv', 'Long Video'),
        ('p', 'Post'),
        ('s', 'Short'),
        ('r', 'Reel'),
        ('st', 'Story'),
    )
    
    channel = models.ForeignKey(MediaPlatform, null=False, blank=False, on_delete=models.CASCADE)
    publish_date = models.DateField(auto_now=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    content_format = models.CharField(max_length=200, choices=FORMAT_CHOICES, default='Long Video')
    status = models.BooleanField(default=True, null=False, blank=False)     
    
    def __str__(self):
        return self.channel.name   
    
class Character(models.Model):
    """
    This model is for having every character or person that inspire you 
    """
    
    TYPE_CHOICES = (
        ('s', 'Stoic'),
        ('ps', 'Psycologist'),
        ('w', 'Writer'),
        ('m', 'Mentor')
    )
    channel = models.ManyToManyField(MediaPlatform, blank=False)
    name = models.CharField(max_length=200, null=False, blank=False)
    character_type = models.CharField(max_length=200, null=False, blank=False, choices=TYPE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} - {self.channel.name}"

class Phrase(models.Model):
    
    """
    This model is for having every phrase that you are going to use to create content 
    """
    
    channel = models.ForeignKey(MediaPlatform, on_delete=models.CASCADE, null=False, blank=False)
    text = models.TextField(blank=False, null=False)
    created_at =  models.DateTimeField(auto_now_add=True)
    is_used = models.BooleanField(default=False)
    date_used = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return self.channel.name
    
class Book(models.Model):
    
    """
    This model is for having every book that you are going to use to create content or for personal use 
    """

    PURPOSE_CHOICES = (
        ('s', 'Spirituality'),
        ('st', 'Stoicicim'),
        ('pg', 'Personal Growth'),
        ('f', 'Financial'),
        ('e', 'Education'),
        ('h', 'Health')
    )
    
    title = models.CharField(max_length=200, null=False, blank=False)
    author = models.CharField(max_length=200, null=False, blank=False)
    purpose = models.CharField(max_length=200, blank=False, null=False, choices=PURPOSE_CHOICES)  
    created_at = models.DateTimeField(auto_now_add=True)  
    
    def __str__(self):
        return f"{self.title} - {self.author}"