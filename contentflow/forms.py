from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm

from .models import Profile, Publication, SocialMedia, VoiceAuthor, MediaPlatform, Subcription, Planning, Account, Prompt, Title, Character, Phrase, Book

class PublicationForm(ModelForm):
    social_media = forms.ModelMultipleChoiceField(
        queryset=SocialMedia.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-control'})

    )
    class Meta:
        model = Publication
        fields = '__all__'
        exclude = ('user', )
        
        widgets ={
            'title': forms.TextInput(attrs={'class': 'form-control my-2'}),
            'slug': forms.TextInput(attrs={'class': 'form-control my-2'}),
            'description': forms.Textarea(attrs={'class': 'form-control my-2'}),
            'script': forms.Textarea(attrs={'class': 'form-control my-2'}),
            'thumbnail_title': forms.TextInput(attrs={'class': 'form-control my-2'}),
            'voice_type': forms.Select(attrs={'class': 'form-select my-2'}),
            'voice_author': forms.Select(attrs={'class': 'form-select my-2'}),
            'voice_name': forms.TextInput(attrs={'class': 'form-control my-2'}),
            'status': forms.Select(attrs={'class': 'form-select my-2'}),
            'content_format': forms.Select(attrs={'class': 'form-select my-2'}),
            'background_music': forms.TextInput(attrs={'class': 'form-control my-2'}),
            'voice_author': forms.Select(attrs={'class': 'form-select my-2'}),
            'social_media': forms.CheckboxSelectMultiple(attrs={'class': ''})
            
        }
class UserProfileForm(forms.ModelForm):
    
    class Meta:
        model =  Profile
        fields = ('avatar', )
        
        widgets = {
            
        }

class UserChangeForm( forms.ModelForm ):
    
    class Meta:
        fields = '__all__'
        exclude =('username', 'password', 'is_superuser',
                  'is_staff', 'is_active', 'groups', 'user_permissions',
                  'date_joined', 'email',)
        
        
        model = User    
        
        widgets ={
            'last_login': forms.TextInput(attrs={'disabled': 'disabled'})
        }    